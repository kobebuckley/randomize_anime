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

#! --------------------------

question = "What type of anime would u like?"
title = "Select One (for now) "
listOfOptions = ["action", "sci-fi"]

choice = eg.multchoicebox(question , title, listOfOptions)

# print("choices are : ", choice)

length_of_choices = len(choice)
# print("length of choices selected are : ", length_of_choices)
dummy_genre = 'action' #make sure all text is lowered by default when taken from user
# dummy_genre_list = ['action', 'mystery'] #make sure all text is lowered by default when taken from user



# dummy_list = str(choice).lower() #just in case, lowering
print("choices are : ", choice)



#! 1/7 - making the list checker comparison --------------------------------------------------------------------------------

# Python3 code to demonstrate working of
# # Test if all elements are present in list
# # Using list comprehension + all()
 
# # initializing list
# target_list = [6, 4, 8, 9, 10]
 
# # initializing test list
# test_list = [4, 6, 9]
 
# # printing lists
# print("The target list : " + str(target_list))
# print("The test list : " + str(test_list))
 


# # Test if all elements are present in list
# # Using list comprehension + all()
# res = all(ele in target_list for ele in test_list)
 
# # Printing result
# print("Does every element of test_list is in target_list ? : " + str(res))




















#! --------------------------------------------------------------------------------------------------------------------------------






# -------------------------------------------------------------------------------------------------------------------------
animeNestedJikan = response.json()['data']

# print("MAIN DATA : ",animeNestedJikan)
lengthOfAnimeAmmt = len(animeNestedJikan
#25 per page
) #36 is the length? 36 animes? no, this is reffering to the first data set of anime. Next would be a looping to find out how many
#! the one above is the key to grabbing each anime set of data
print("The amount of animes available are: ", lengthOfAnimeAmmt)

#! making a loop to grab the above data but for each anime


# print(animeNestedJikan)

# animeNestedJikanGroups = []

#! looping through each anime group, 0 1 2 3 etc., then checking if genres match with user input, then adding it to a new array if it does and moving on to next, otherwise moving on to next 
counter = 0

genreCounter = 0

new_list = []
unique_list = set(new_list)
# currentSelection = []
# finalSelection = []

# for x in animeNestedJikan[:]:
#! need to find out why genre isn't properly working - 5:25 - 1/5


while counter < lengthOfAnimeAmmt:
    # genreCounter = 0
    print("counter is now:", counter)
    # print("Counter is : ", counter)
#     #! new anime checked each loop 
#     print("here is each anime : ",animeNestedJikan[counter])
#     #! checking the genres
    # print("THE GENRE/S IT CONTAINS is/are HERE---------------------------------------------",animeNestedJikan[counter]['genres'])
      #! figuring out the length of how many genres are in this set : not including "explicit genre types such as more in depth like space for example"
    genreLength = len(animeNestedJikan[counter]['genres'])
    print("amount of genres are : ", genreLength)



    # print("amount of genres are : ", genreLength)

    print("genre counter is : ",genreCounter)
    while genreCounter < genreLength:
#         # genres_available = animeNestedJikan[counter]['genres']
# #! seems to only grab one genre, needs all of the genres from the list - 1/5 5:53
#         genres_available = animeNestedJikan[counter]['genres'][genreCounter]
        genres_available = animeNestedJikan[counter]['genres'][genreCounter]

        print("name : ",genres_available['name'] )
        # temp_name_holder = []
        temp_name_holder = str(genres_available['name']).lower()
        new_list.append(temp_name_holder)
        unique_list = set(new_list)
        genreCounter+=1
    print("new list is, ", unique_list)
    result = all(ele in unique_list for ele in choice)
    if result == True:
        print("SUCCESS! ALL WERE FOUND")
        genreCounter = 0
        counter +=1
        new_list = []
    else:
        print("NOT ALL WERE FOUND")
        genreCounter = 0
        counter +=1
        new_list = []

    
#         temp_list_checker = new_list.append(genres_available)
#         print("NEW LIST : ", temp_list_checker)
# #         print(genreCounter,"counter genre here: ",genres_available[genreCounter])

#         # Test if all elements are present in list
#         # Using list comprehension + all()
#         result = all(ele in genres_available for ele in choice)
 
#         # Printing result
#         print("Is every element of choice in genres_available? : " + str(result))





    #     if result == True:
    #             print("all choices were found!")
    #     if genreCounter < genreLength:
    #             print("not all choices were found : ", str(choice).upper())
    #             print("the genres found in this anime are : ", str(genres_available['name']).upper())
    #             genreCounter +=1

    # # genreCounter+=1

    #     else:
    #         print("done with the genres in this anime, moving onto next anime, also sidenote that we need to add to / keep in a set")
    #         genreCounter = 0
    #         counter+=1
        







# # loop version
# # for eachChoice in choice:
#     if dummy_genre in genres_available:
#         print("dummy text was found!")
#     else:
#         print("dummy text not found")

# # # change below to anime genre looping
# # for eachChoice in choice:
# #     if dummy_genre in choice:
# #         print("dummy text was found!")
# #     else:
#         print("dummy text not found")

# change below to anime genre looping
# for eachChoice in choice:
#     if dummy_genre_list in choice:
#         print("dummy text list was found!")
#     else:
#         print("dummy text list not found")

        #! The loop is working! Need to add in the checker for the dummy text to see if the anime contains the text in at least on eof the genres, once it does, the loop can stop (or not) and put the anime into a set

        # # while counter < lengthOfAnimeAmmt:
        # print("amount of genres are : ", genreLength)
        # print("the genre names in this anime are: ", genres_available)
        # print("counter is now:", counter)
        # while genreCounter < len(genres_available):
        #     print("here is genre counter",genreCounter)
        #     name_of_genre=genres_available[genreCounter]['name']
        #     print('Here is the name of the specific genre name: ', name_of_genre)
        #     genreCounter+=1

    #! place to add in the genre checker
    
#     #? will need to make the string all undercase at some point
#         if animeNestedJikan[counter]['genres'][genreCounter]['name'].lower() in (dummy_genre.lower()):

# # #? will need to do this check for each single anime (so we need it to be included in the larger loop by somehow grabbing only a single piece of data for each anime throughout the loop)

# #! if at least one works, then add to a new array called "currentSelection", otherwise it wont be added. So we need to add a "break" so it won't keep adding more
        
#             print("Dummy Text FOUND : ", dummy_genre, "The anime genre is: ", animeNestedJikan[counter]['genres'][genreCounter]['name'].lower())
#             counter += 1
#             print("counter is : ",counter)
            

        
#         else:
           
#             print("Dummy Text NOT-----FOUND : ", dummy_genre, "The anime genre is: ", animeNestedJikan[counter]['genres'][genreCounter]['name'].lower())
#             genreCounter+= 1
#             print("changing genre counter to:", genreCounter)
#             print("counter is : ",counter)


      
        
        
        #! MAYBE USE PYTHON FILTER INSTEAD OF LOOPING? AND CHECK OUT THIS PAGE IF NEEDED - https://api.jikan.moe/v4/genres/anime
        
        

# print(len((finalSelection)))
   
        # break 

    # print(currentSelection)
    # print("working after the break? : ", len(currentSelection) )
    #! end of loop to find the genre names
    # counter += 1
    
#! not sure what the point of genreCounter is for, seems to mess it up when I use it
# print("final selection is : ", finalSelection)
# print("current selection has : ", len(currentSelection) ," animes inside of it (+ 1?)")
# print(currentSelection)




#--------------------------------------------------------------------------------------------------------------









# #simpler loop that includes a Set
# animeNestedJikan = response.json()['data']

# counter = 1
# genreCounter = 0
# #if includes...
# print("test: ", animeNestedJikan[counter]['genres'][genreCounter]['name'])

# for individual_anime in animeNestedJikan[0]['mal_id'][0]:
#     print ("individual anime",individual_anime)
    # for individual_genres in individual_anime:
    #     print("genres : ", individual_genres)
        # for genre_list in individual_genres:
        #     print("genre list ",genre_list)
            # for genre_name in genre_list:
            #     print("name of genre is: ",genre_name)
        # if dummy_genre in genre_list:
        #     print('DUMMY TEXT HAS BEEN FOUND! ADD ME, THEN CONVERT TO A SET?')

    #each anime has been grabbed, now needing to check the genre of each one at a time and ouput it to test, then check it against user input choice


    # if animeNestedJikan[individual_anime]['genres']

# # for x in animeNestedJikan[:]:
# while counter < lengthOfAnimeAmmt:
#     # print("Counter is : ", counter)
# #     #! new anime checked each loop 
# #     print("here is each anime : ",animeNestedJikan[counter])
# #     #! checking the genres
#     # print("THE GENRE/S IT CONTAINS is/are HERE---------------------------------------------",animeNestedJikan[counter]['genres'])
#       #! figuring out the length of how many genres are in this set 
#     genreLength = len(animeNestedJikan[counter]['genres'])
#     # print("amount of genres are : ", genreLength)
#     while genreCounter < genreLength:
#     # print("each individual here : ",animeNestedJikan[counter]['genres'][genreCounter]['name'])
#     #! place to add in the genre checker
    
#     #? will need to make the string all undercase at some point
#         if animeNestedJikan[counter]['genres'][genreCounter]['name'].lower().__contains__(choiceString.lower()):

# # #? will need to do this check for each single anime (so we need it to be included in the larger loop by somehow grabbing only a single piece of data for each anime throughout the loop)

# #! if at least one works, then add to a new array called "currentSelection", otherwise it wont be added. So we need to add a "break" so it won't keep adding more
#             # print("String contains target!")
#             # print(animeNestedJikan[counter])
#             currentSelection.append(animeNestedJikan[counter])
#             break 
#         #! it only breaks the loop inside of itself, not all of them, should break because it meets the requirements
#             # print("the data: ", animeNestedJikan[counter])
#             # currentSelection = (animeNestedJikan[counter])
#             # finalSelection.append(currentSelection)
            
#             # print("Anime that meets at least one of the requirements : ",currentSelection)
            
        
#         else:
#             # print("String does not contain target", counter)
#             # print("NOW REMOVING FROM LIST : ",animeNestedJikan.remove(animeNestedJikan[counter]))
#             # print("hmm : ", animeNestedJikan[counter])
#             # animeNestedJikan[counter].clear()
            
#             # print("Genres it does contain : ",animeNestedJikan[counter]['genres'] )
#             print("genre counter is : " , genreCounter , "!!!!!!!!!!!!!!")
#             break
        
        
        





































# print("choice selected : ",choice)
# choiceString = str(choice[0])
# print("choice string : ",choiceString)



#! --------------------------

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


# print("final selection is : ", len(finalSelection))

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