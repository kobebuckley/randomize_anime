from random import choice
import requests

# panda imports
import numpy as np
import pandas as pd

#jikan - anime api

#! the url query (?) should change depending on the checbox inputs of the user. 
#! the anime page also has multiple pages, so that needs to be accounted for when it comes down to all the data (likely chaning the Pagination will be the key?)

#! Then it should return the main info (TBA - name, genre, length(depending on certain integers), series vs movie, etc., )

response= requests.get('https://api.jikan.moe/v4/anime') # getAnimeSearch on Jikan is the most likely relevant part to continue this project 
response.status_code

#! ?genres=1  -> possible query to add to the above url ?genres=choice[]???

#! genre - name


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
filtered_anime_list = []
unique_filtered_anime_list = set(filtered_anime_list)


testing_data = []


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
        temp_anime_holder = animeNestedJikan[counter]
        print("current anime being checked is : ", animeNestedJikan[counter]['url'])
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
        testing_data.append(animeNestedJikan[counter])
        filtered_anime_list.append(animeNestedJikan[counter]['url']) # adding this specific anime that meets the above conditions into the filtered list
        unique_filtered_anime_list = set(filtered_anime_list)
        print("the new current anime list is: ", unique_filtered_anime_list)
        genreCounter = 0
        counter +=1
        new_list = []
    else:
        print("NOT ALL WERE FOUND")
        genreCounter = 0
        counter +=1
        new_list = []


print("The amount of anime that meet your selections are: " , len(unique_filtered_anime_list))

#! maybe can randomize through all the data and send each option back? Similar to what is below this
print("*** Url for the anime selected is :" , (testing_data[7]['url']))
print("*** Japanese Title for the anime selected is:" , (testing_data[7]['title_japanese']))
print("*** English Title for the anime selected is:" , (testing_data[7]['title_english']))
#! can make a fuction for the above code, for printing out miltiple pieces of data




# # advanced (apit] - dataframes)
# # jikan

# #pandas
#pandas - dataframe





#? STARTING NEW VERSION HERE, TO EVENTUALLY CONVERT FROM THE TOP SECTION

# import numpy as np
# import pandas as pd

# df = pd.DataFrame(unique_filtered_anime_list)
# # df.head()

# print("pandas data frame here: ", df.head())