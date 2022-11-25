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



        
# animeNested = [
# ["naruto","comedy","long","series"], 
# ["jujutsu kaisen","action","short","movie"], 
# ["chainsaw man","Action","medium","series"] 
# ]



# #! important query section
# mood = input("What mood are u looking for?")
import easygui as eg

question = "What type of anime would u like?"
title = "Select One (for now) "
listOfOptions = ["Action", "comedy", "sci-fi"]

choice = eg.multchoicebox(question , title, listOfOptions)

print("choice selected : ",choice)
choiceString = str(choice[0])
print("choice string : ",choiceString)

# practiceUrlString = "test"
# print("The original string : " + str(practiceUrlString))
# print("The add string : " + str(choiceString))

# practiceUrlString += choiceString
# print("The concatenated string is : " + practiceUrlString)


# # #? Maybe adding the choice value to the Jikan url query? to then pull data from that category
# # #? Python | Add one string to another
# # #! important query section






# # print(choice[0])

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


#! making a large loop that does everything needed instead of splitting it up between multiple variables

#? going to need to loop through to find each anime on the page before adding the rest of the steps (later will need to search through pages)

animeNestedJikan = response.json()['data']

# print("MAIN DATA : ",animeNestedJikan)
lengthOfAnimeAmmt = len(animeNestedJikan) #36 is the length? 36 animes? no, this is reffering to the first data set of anime. Next would be a looping to find out how many
#! the one above is the key to grabbing each anime set of data

#! making a loop to grab the above data but for each anime


# print(animeNestedJikan)

# animeNestedJikanGroups = []

counter = 0
#! looping through each anime group, 0 1 2 3 etc., then checking if genres match with user input, then adding it to a new array if it does and moving on to next, otherwise moving on to next 

currentSelection = []

# print(lengthOfAnimeAmmt)
# print(animeNestedJikan[0]['genres'][genreCounter]['name'])

genreCounter = 0


# for x in animeNestedJikan[:]:
# while counter < lengthOfAnimeAmmt:
#     #! new anime checked each loop 
#     print("here is each anime : ",animeNestedJikan[counter])
#     #! checking the genres
print("THE GENRE/S IT CONTAINS is/are HERE---------------------------------------------",animeNestedJikan[counter]['genres'])
      #! figuring out the length of how many genres are in this set 
genreLength = len(animeNestedJikan[counter]['genres'])
print("amount of genres are : ", genreLength)
while genreCounter < genreLength:
    # print("each individual here : ",animeNestedJikan[counter]['genres'][genreCounter]['name'])
    #! place to add in the genre checker
    
    #? will need to make the string all undercase at some point
    if animeNestedJikan[counter]['genres'][genreCounter]['name'].__contains__(choiceString):

# #? will need to do this check for each single anime (so we need it to be included in the larger loop by somehow grabbing only a single piece of data for each anime throughout the loop)

        print("String contains target!")
    else:
        print("String does not contain target")


    
    genreCounter += 1 
    #! end of loop to find the genre names
    
    
#     counter += 1
#     #! end of loop 

    # currentSelection = animeNestedJikan[:counter]
    # print("here is the current selection : ",currentSelection)
#     # animeNestedJikanGroups.append(animeNestedJikan[:counter])
    # counter += 1
#     # animeNestedJikanGroups = animeNestedJikan[:counter]
#     # print(animeNestedJikanGroups)
    
    # print("HERE IS THE GENRE", animeNestedJikanGroups['genres'])
    # animeNestedSingular = animeNestedJikanGroups[:counter].append(['genres'])
    # print("HERE IS THE SINGULAR GENRE :",animeNestedSingular )
    # print(animeNestedJikanGroups[:counter]['genres'])
    # if (animeNestedJikanGroups[:counter].__contains__(choiceString)):
    #     print("String contains target!")
    # else:
    #     print("String does not contain target")

# print("Here is the group of all the animes on this page : ", animeNestedJikanGroups)



# while counter < lengthOfGenre:
#     genreArrayData.append(OriginalGenreData[counter])
#     counter += 1
#     genreArrayData = genreArrayData[:counter]
# print("The different genres in this anime are: ", genreArrayData)


# print("HERE IS THE LENGTH : ",lengthOfAnimeAmmt)
# print("Here is what length is reffering to : ", animeNestedJikan)
# print("HERE IS WHAT THE - animeNestedJikanGroups is referring to", animeNestedJikanGroups[1]['genres'][0]['name'])















#!----------------------------------------


# #? will need to make the string all undercase at some point
# # if animeNestedJikanGroups[1]['genres'][0]['name'].__contains__(choiceString):

# #? will need to do this check for each single anime (so we need it to be included in the larger loop by somehow grabbing only a single piece of data for each anime throughout the loop)

#     print("String contains target!")
# else:
#     print("String does not contain target")


# #! Now we need to sift through the JikanGroups for each anime to then compare it against the user inputs 
# counter = 0
# lengthOfAnimeJikanGroupAmmt = len(animeNestedJikanGroups)





#!----------------------------------------





# animeNestedJikanGroupsSingledOut = animeNestedJikanGroups[:counter]["mal_id"]


# while counter < lengthOfAnimeJikanGroupAmmt:
#     animes.append(OriginalGenreData[counter])
#     counter += 1
#     genreArrayData = genreArrayData[:counter]
# print("The different genres in this anime are: ", genreArrayData)


# print("HERE IS THE LENGTH : ",lengthOfAnimeAmmt)
# print("Here is what length is reffering to : ", animeNestedJikan)










# for x in animeNestedJikan[:]:
#    animeNestedJikanGroups
    

# # OriginalAllSingleAnimeData = response.json()['data'][0]
# # print("ALL THAT ONE ANIME DATA!! : ", OriginalAllSingleAnimeData)


# # OriginalAnimeData = response.json()['data'][0]['title']
# # print("ORIGINAL DATA NAMES HERE", OriginalAnimeData)
# # OriginalGenreData = response.json()['data'][0]['genres']
# # OriginalDataSetCombo = str(OriginalGenreData) + str(OriginalAnimeData)
# # print("COOOOOOOOMBOOOOOOOO",OriginalDataSetCombo)
# # # v2OriginalGenreData = response.json()['data'][0]['genres'][0]['name'] #! working version to grab data
# # # print("LOOK HERE")
# # # print(v2OriginalGenreData)
# # print("LOOK HERE")

# #! successfuly grabbed the specific genre data that will have to match up / contain same checkbox data. 
# # #? add in multiple mal_id? like the animeNested version 
# lengthOfGenre = len(OriginalGenreData)
# print(lengthOfGenre)

# genreArrayData = []

# counter = 0

# while counter < lengthOfGenre:
#     genreArrayData.append(OriginalGenreData[counter])
#     counter += 1
#     genreArrayData = genreArrayData[:counter]
# print("The different genres in this anime are: ", genreArrayData)

# #! removing genres / anime that does not align with what the user wants

# #! looping the name variables of the genres 

# genreNamesOnlyArray = []
# lengthOfNames = len(genreArrayData)
# print("HERE IS THE LENGTH : ",lengthOfNames)
# counter = 0

# while counter < lengthOfNames:
#     genreNamesOnlyArray.append(genreArrayData[counter]['name'])
#     counter +=1
#     genreNamesOnlyArray = genreNamesOnlyArray[:counter]

# # genreNamesOnlyArray = genreArrayData[0]['name']
# print("here are the names of the genre : ", genreNamesOnlyArray)

# # !removing what does not match from the list 

# for x in genreNamesOnlyArray[:]: 
#     print("here is the X variable : ",x)
#     if x != choiceString:
#         genreNamesOnlyArray.remove(x)

# print("nested below")
# print(genreNamesOnlyArray[0])   
        


# #! add the original data back and return whatever data is relevant (for now just return the name of the animes that meet the req, and later can add more stuff and randomize etc., )

# #! looping the name variables of the anime 

# # genreNamesOnlyArray = []
# # lengthOfNames = len(genreArrayData)
# # print("HERE IS THE LENGTH : ",lengthOfNames)
# # counter = 0

# # while counter < lengthOfNames:
# #     genreNamesOnlyArray.append(genreArrayData[counter]['name'])
# #     counter +=1
# #     genreNamesOnlyArray = genreNamesOnlyArray[:counter] = []

    
# #! simple method - might have been the easiest way from the start???

# #   my_str = "Hello from AskPython"
 
# # target = "AskPython"
 
# if (animeNestedJikanGroups[:counter].__contains__(choiceString)):
#     print("String contains target!")
# else:
#     print("String does not contain target")













        
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