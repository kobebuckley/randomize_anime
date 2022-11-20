from random import choice
import requests



#jikan - anime api


#! the url query (?) should change depending on the checbox inputs of the user. 

#! Then it should return the main info (TBA - name, genre, length(depending on certain integers), series vs movie, etc., )

response= requests.get('https://api.jikan.moe/v4/anime') # getAnimeSearch on Jikan is the most likely relevant part to continue this project 
response.status_code







        
animeNested = [
["naruto","comedy","long","series"], 
["jujutsu kaisen","action","short","movie"], 
["chainsaw man","action","medium","series"] 
]

animeNestedJikan = []



# mood = input("What mood are u looking for?")
import easygui as eg

question = "This is your question"
title = "This is your window title"
listOfOptions = ["action", "comedy", "option 3"]

choice = eg.multchoicebox(question , title, listOfOptions)

print(choice)
choiceString = str(choice[0])

practiceUrlString = "test"
print("The original string : " + str(practiceUrlString))
print("The add string : " + str(choiceString))

practiceUrlString += choiceString
print("The concatenated string is : " + practiceUrlString)


#? Maybe adding the choice value to the Jikan url query? to then pull data from that category
#? Python | Add one string to another






# print(choice[0])

# #? currently working for singular inputs, but multiple selections is not showing properly
# #? the above problem might be solved by moving onto using the real data inputs

# for x in animeNested[:]: # removing what does not match from the list 
#     # print(x)
#     if x[1] != choice[0]:
#         animeNested.remove(x)

# print("nested below")
# print(animeNested)   
        

# print(response.status_code)

# print(response.json())

# html_text = response,params={'genres'}).text
# print(html_text)


malId = response.json()['data'][0]['mal_id']
# malId = response.json()['genres']
print(malId)


















        
        # --------------------------------------------------------------------------------------
        
        
        
        
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
#pandas - dataframe