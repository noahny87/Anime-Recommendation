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
0           Project ARMS   [[0.9839145]]
1              Wolverine  [[0.98117644]]
2          Speed Grapher   [[0.9810757]]
3              Fate/Zero  [[0.97979856]]
4                Slayers  [[0.97923565]]
5  Chrome Shelled Regios   [[0.9786517]]
6               Kurozuka  [[0.97846365]]
7         Haibane Renmei   [[0.9774355]]
8           Overlord III   [[0.9773185]]
9            Double Hard   [[0.9769054]]

It displays Anime Name and then Similarity Score (1 is perfect 0 is worst) 
