from random import choice
import requests



#jikan - anime api

#! the url query (?) should change depending on the checbox inputs of the user. 
#! Then it should return the main info (TBA - name, genre, length(depending on certain integers), series vs movie, etc., )

response= requests.get('https://api.jikan.moe/v4/anime') # getAnimeSearch on Jikan is the most likely relevant part to continue this project 
response.status_code



# print(response.status_code)

# print(response.json())

# html_text = response,params={'genres'}).text
# print(html_text)


malId = response.json()['data'][0]['mal_id']
# malId = response.json()['genres']
print(malId)


#pandas - dataframe