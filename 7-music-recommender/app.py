import random

print('music-recommender')

genres = {'rock': ["AC/DC", "Queen", "Led Zeppelin"], 
          'pop': ["Taylor Swift", "Ariana Grande", "Dua Lipa"],  
          'hip-hop': ["Kendrick Lamar", "Drake", "J. Cole"]}

choice = input("choose a genre (rock, pop, hip-hop) ")

if choice not in genres:
    print("invalid genre. please choose from rock, pop, or hip-hop.")
else:
    print(f"check out {random.choice(genres[choice])} ")