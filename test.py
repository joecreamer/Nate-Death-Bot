import requests
import json

name = input("Enter Player Name: ")
tagline = input("Enter Player Tagline: #")
api_key = "RGAPI-0633d379-f1ad-438b-b6d6-b5cd80261646"
url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tagline}?api_key={api_key}"
# url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/crispyvevo/NA1?api_key={api_key}"
request = requests.get(url)
jsonrequest = request.json()
print(jsonrequest)
"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/thefrylock/8842?api_key=RGAPI-0633d379-f1ad-438b-b6d6-b5cd80261646"



# for key, value in jsonrequest[0].items():
#     print(f"{key}: {value}")