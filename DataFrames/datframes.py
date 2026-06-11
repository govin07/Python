import pandas as pd 
import numpy as np

# studen = [
#     [100, 80,10],
#     [90,70,7],
#     [120,100,14],
#     [80,50,2]
# ]

# total = pd.DataFrame(studen, columns=['id','marks','package'])

# # print(total)

# student_dict = {
#     'id':[100,90,70,80],
#     'marks':[80,20,50,40],
#     'package': [12,15,50,60]
# }

# our = pd.DataFrame(student_dict)
# # print(our)

movies = pd.read_csv('movies.csv')
ipl = pd.read_csv('ipl-matches.csv')
# # print(movies)
# # print(ipl)

# # shape

# # print(movies.shape)

# # dtypes

# # print(movies.dtypes)

# # index

# # print(movies.index)

# # info

# # print(movies.info())

# # .isnull

# # print(movies.isnull())

# # single colm

# # print(movies['title_x'])

# # row

# # print(movies.iloc[0])

# # print(ipl.head(2))
# mask = ipl['MatchNumber'] == 'Final'
# ndf = ipl[mask]

# # print(ndf[['Season', 'WinningTeam']])

# ny = ipl['SuperOver'] == 'Y'
# naa = ipl[ny]
# # print(naa.shape[0])

# ct = ipl["City"] == 'Kolkata' 
# wn = ipl["WinningTeam"] == "Chennai Super Kings"
# fn = ipl[ct & wn]
# # print(fn)
# toss  = ipl['TossWinner'] == ipl['WinningTeam']

# # print(ipl[toss])

# spl = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
# rat = movies['imdb_rating'] > 7.5
# # print(movies[spl & rat])

# ###


