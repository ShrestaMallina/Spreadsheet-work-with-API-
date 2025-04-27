import os
import requests
from datetime import datetime



#personal data to calculate calories
GENDER = "female"
WEIGHT = 67,
HEIGHT = 168,
AGE=23,
APP_ID =os.environ["APP_ID"]
API_KEY=os.environ["API-KEY"]
AUTH_TOKEN_BASIC = os.environ["AUTH_TOKEN_BASIC"]


Nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_params = {
         "query":input("Tell me which exercise you did?"),
         "gender":GENDER,
         "weight_kg":WEIGHT,
         "height_cm":HEIGHT,
         "age":AGE,
}



headers ={
     "Content-Type": "application/json",
     "x-app-id" : APP_ID,
    "x-app-key": API_KEY,
    "Authorization":AUTH_TOKEN_BASIC,
}


response = requests.post(url=Nutrition_endpoint,json=nutrition_params,headers=headers)
data = response.json()


SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
today = datetime.now()
THIS_DAY = today.strftime("%d/%m/%Y")
TIME_TODAY = today.strftime("%H:%M:%S")
for exercise in data["exercises"]:
    request_body ={
         "workout":{
                  "date":THIS_DAY,
                  "time":TIME_TODAY,
                  "exercise":exercise['name'],
                  "duration":exercise['duration_min'],
                  "calories":exercise['nf_calories'],
        }
    }
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
sheety_response = requests.post(url=SHEET_ENDPOINT,json=request_body,auth=(f'{USERNAME}',f'{PASSWORD}'))
sheet_data = sheety_response.json()







