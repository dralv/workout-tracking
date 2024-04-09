import os
import requests

app_id = os.environ['APP_ID_NUTRITIONIX']
api_key = os.environ['API_KEY_NUTRITIONIX']

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    'x-app-id':app_id,
    'x-app-key':api_key
}
query = input("Tell me which exercises you did: ")
body = {
    "query": query
}
response = requests.post(url=url,headers=headers,json=body)
print(response.text)
