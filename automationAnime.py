from random import choice
import requests



#jikan - anime api


#! the url query (?) should change depending on the checbox inputs of the user. 
#! the anime page also has multiple pages, so that needs to be accounted for when it comes down to all the data (likely chaning the Pagination will be the key?)

#! Then it should return the main info (TBA - name, genre, length(depending on certain integers), series vs movie, etc., )

response= requests.get('https://api.jikan.moe/v4/anime') # getAnimeSearch on Jikan is the most likely relevant part to continue this project 
response.status_code

#! ?genres=1  -> possible query to add to the above url ?genres=choice[]???

#! genre - name



        
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
#? add themes on top of genres at some point?
OriginalGenreData = response.json()['data'][0]['genres']

# genreData = response.json()['data'][0]['genres'][1] #! successfuly grabbed the specific genre data that will have to match up / contain same checkbox data. 
# #? add in multiple mal_id? like the animeNested version 
# # malIdMultiple = response.json()['data'][1]['genres'][0]['mal_id'] 
# # malId = response.json()['genres']
# print(genreData)
# # print(malIdMultiple)

# lengthOfGenre = len(OriginalGenreData)
# print("There are : ")
# # print(lengthOfGenre)
# print(" genres in this anime!")
# for x in OriginalGenreData[:]: # looping to find the length and return that id  
lengthOfGenre = len(OriginalGenreData)
print(lengthOfGenre)

genreArrayData = []

counter = 0

while counter < lengthOfGenre:
    genreArrayData.append(str(OriginalGenreData[counter]))
    counter += 1
    genreArrayData = genreArrayData[:counter]
print("The different genres in this anime are:", genreArrayData)




    
# #     if x[1] != choice[0]:
# #         animeNested.remove(x)




#? testing to check for specific data values such as the mal id  out of the data
# # newData = [obj for obj in genreData if 'mal_id' in obj[0]]
# testing = genreData['mal_id'] # the exact data from this id is here
# print("New Data below : ")
# print(testing)
# # print(newData)


#! the mal_id for the genre should match up with the value/s the user input. 


















        
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