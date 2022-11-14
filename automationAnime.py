from random import choice
import requests















#jikan - anime api

response= requests.get('https://api.jikan.moe/v4/anime') #! getAnimeSearch on Jikan is the most likely relevant part to continue this project 
response.status_code



# print(response.status_code)

# print(response.json())

# html_text = response,params={'genres'}).text
# print(html_text)


# malId = response.json()['data'][0]['mal_id']
malId = response.json()['genres']
print(malId)


#pandas - dataframe