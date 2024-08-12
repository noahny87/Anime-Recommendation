#Create recommendation system using KNN and cosine similarity 
#First preprocess and embed all the data 
#Construct a KNN model to predict what a user would like to watch based on input of tv show

import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

def preprocess(df):
    cols = ["MAL_ID","Japanese name", 'Licensors','Studios', 'Source', 'Popularity', 'Completed', 'On-Hold', 'Dropped','Plan to Watch', 'Rating','Members', 'Favorites'] #get rid of extra columns
    df = df.drop(cols,axis=1)
    score_list2 = ['Score-10', 'Score-9', 'Score-8', 'Score-7', 'Score-6', 'Score-5', 'Score-4', 'Score-3', 'Score-2', 'Score-1']#going to get rid of all score columns 
    score_list = ['Score-10', 'Score-9']#since scores are kind of arbitrary going to only use top 2 score columns to assign score to anime show 
    unknown = {"Unknown":0}#map unknown variables to 0
    df[score_list].map(lambda x: unknown.get(x) if x in unknown else x)#apply map using lambda 
    df[score_list] = df[score_list].apply(pd.to_numeric, errors='coerce')#since some of the data is super messy we need to coerce rows to nan values 
    #print(df[score_list].head(-10))#look at top 10 rows
    #df[score_list] = df[score_list].apply(lambda x: x.replace("Unknown",0))
    df["Score"] = df[score_list].mean(axis=1)#apply mean to get score column
    df = df.drop(score_list2,axis =1)#drop all the score columns 
    #print(df.head())
    return df 
def embed(df):
    #now to embed the data
    #we want to change the data from separate columns to a single column i.e. a corpus 
    df1 = df[['Name', 'Score', 'Genres', 'English name', 'Type', 'Episodes', 'Aired','Premiered', 'Producers', 'Duration', 'Ranked', 'Watching']]
    df1 = df1.apply(lambda x: ','.join(x.astype(str)), axis=1)
    df1 = pd.DataFrame({'clean': df1})
    #create list of list 
    df1 = [row.split(",") for row in df1['clean']]
    #print(df1[:2])
    #train word2vec model
    model = Word2Vec(df1, min_count=1, vector_size= 100,workers=5, window =5, sg = 1)
    print(model.wv)# while training we can see that the similarity between Dragon Ball and Dragon Ball GT is 0.9 - wv.similarity is good but cosine similarity is better
    #using sklearn cosine similarity we can get more accurate similarities between anime shows
    return model
    
def cs_similarity(model,input,num,anime):
    top10dict = {}
    #get top 10 similar anime
    input_vectors = model.wv[input]#need to get input vectors from the model 
    #get most similar by getting vectors of all anime and computing cosine similarity
    for item in anime:
        if item != input and item in model.wv:
            output_vectors = model.wv[item]
            #calculate cosine similarity
            sim = cosine_similarity(input_vectors.reshape(1,-1),output_vectors.reshape(1,-1))
            top10dict[item] = sim#create dictionary of all anime and their similarity scores
            #sort to get top 10
    top10 = sorted(top10dict.items(), key=lambda x: x[1], reverse=True)
    top10 = pd.DataFrame.from_dict(top10[:num])
    print(top10)#what is the most similar to Naruto 




def main():
    df = pd.read_csv("C:\\Users\\noahn\\OneDrive\\Documents\\Pythonprojects\\.venv\\anime.csv")
    df = preprocess(df)#preprocess data
    #print(df.columns)
    #embed(df)
    anime = list(df['Name'].unique())#get list of all anime for cosine similarity later
    model = embed(df)
    cs_similarity(model,"Samurai Champloo",10,anime)
    #embed the data

if __name__ == "__main__":
    main()



