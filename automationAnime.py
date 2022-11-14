from random import choice
import requests

#jikan - anime api

response= requests.get('https://api.jikan.moe/v4/anime/20')
response.status_code



print(response.status_code)

# print(response.json())

malId = response.json()['data']['mal_id']
print(malId)
#pandas - dataframe