from random import choice
        
animeNested = [
["naruto","comedy","long","series"], 
["jujutsu kaisen","action","short","movie"], 
["chainsaw man","action","medium","series"] 
]


# mood = input("What mood are u looking for?")
# import easygui as eg

# question = "This is your question"
# title = "This is your window title"
# listOfOptions = ["action", "comedy", "option 3"]

# choice = eg.multchoicebox(question , title, listOfOptions)

print(choice)
# print(choice[0])

#? currently working for singular inputs, but multiple selections is not showing properly
#? the above problem might be solved by moving onto using the real data inputs

for x in animeNested[:]: # removing what does not match from the list 
    # print(x)
    if x[1] != choice[0]:
        animeNested.remove(x)

print("nested below")
print(animeNested)   
        
#         #! now needing to take that list and loop through it to find the length input match.
# length = input("What length are u looking for?")


# for x in animeNested[:]: # removing what does not match from the list 
#     # print(x)
#     if x[2] != length:
#         animeNested.remove(x)

# print("nested below length version")
# print(animeNested)   
        
#         #! now needing to take that list and loop through it to find the animeType input match.
        
# animeFormat = input("Do you want a series or a movie?")


# for x in animeNested[:]: # removing what does not match from the list 
#     # print(x)
#     if x[3] != animeFormat:
#         animeNested.remove(x)

# print("nested below anime format version")
# print(animeNested)   



# # advanced (apit] - dataframes)
# # jikan

# #pandas