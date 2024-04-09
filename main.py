import os
import requests
from datetime import datetime
def getting_exercises():
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
    response = requests.post(url=url,headers=headers,json=body).json()
    data = response['exercises']
    return data

def get_exercises_stats(data):
    exercises = [{"exercise":d['name'],"duration":d['duration_min'],"calories":d['nf_calories']} for d in data]
    return exercises
def write_sheet(exercises):
    now = datetime.now()
    today = now.strftime('%d/%m/%Y')
    hour = now.strftime('%H:%M:%S')
    auth = os.environ['SHEETY_AUTH']
    sheety_url = "https://api.sheety.co/028889e3f0eb8904732d082a6fb699e9/myWorkouts/workouts"
    headers = {
        "Authorization": auth
    }
    for e in exercises:

        body = {
            "workout":{
                "date":today,
                "time":hour,
                "exercise": e['exercise'].title(),
                "duration":e['duration'],
                "calories":e['calories']
            }
        }

        requests.post(url=sheety_url,json=body,headers=headers)

data = getting_exercises()
exercises = get_exercises_stats(data)
write_sheet(exercises)


