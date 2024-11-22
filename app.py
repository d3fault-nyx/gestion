import requests
import json

url = "https://official-joke-api.appspot.com/random_joke"

reponse = requests.get(url)

if reponse.status_code == 200: 
    reponse_json = json.loads(reponse.text)
    print(reponse_json["setup"])
    print(reponse_json["punchline"])

else :
    print("erreur")