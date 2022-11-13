from random import choice



# Base Project:
        
#         1. Put all recommended anime in a list in Python 
anime = ["naruto", "jujutsu kaisen", "chainsaw man"];
#         2. Randomly choose one and print
# print(choice(anime));


# base project completed 



#   Upgraded Project:
        
#         1. Make a sublist with anime parameters (nested list) / later replace with variables that are not strings
animeNested = [
[["naruto"],["comedy"],["long"],["series"]], 
[["jujutsu kaisen"],["action"],["short"],["series"]], 
[["chainsaw man"],["action"],["short"],["series"]] 
]

#         2. Use the input function (mood, runtime, series/movie)heavy

mood = input("What mood are u looking for?")
print("Mood selected is", mood)
#         3. Loop to find the mood that matches the input (can be type but maybe a different input )

print(choice(animeNested[0][0]));
