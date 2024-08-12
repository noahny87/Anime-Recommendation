Hello this fun project is an Anime recommendation system just input an anime that you like and it will output 10 similar anime's!

I am a HUGE fan of Naruto and wanted to put my skills to the test with creating something like they have one websites and online in general.
Most sites recommending anime's similar to Naruto are blogs without any data backing the claims so here i decided to see what the data would tell me.

To get the Data I went to kaggle and got it here:https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020
Then I knew I needed to create a vectorized matrix/list of the words 
Finally I had to create a similarity model and I knew about cosine similarity from a previous project along with use of K-NN algorithm.
So i implemented the cosine similarity idea and got my final project! 
Overall a really fun project and super helpful!

P.S. More documentation is in the code of what is going on 😊

P.P.S Here is my answer for what is similar to the anime "Naruto":
                0               1
0  Dragon Ball Super  [[0.97753817]]
1     Akame ga Kill!   [[0.9766468]]
2      Speed Grapher   [[0.9756323]]
3            Radiant  [[0.97426593]]
4         D.Gray-man   [[0.9740176]]
5  Ninja Hattori-kun   [[0.9731953]]
6      Dragon League   [[0.9727888]]
7      Rental Magica   [[0.9725962]]
8          Gatchaman   [[0.9724921]]
9       Project ARMS   [[0.9723543]]

It displays Anime Name and then Similarity Score (1 is perfect 0 is worst) 
