import requests
from bs4 import BeautifulSoup

# link = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/thefrylock/8842?api_key=RGAPI-0633d379-f1ad-438b-b6d6-b5cd80261646"
link = "https://americas.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=RGAPI-0633d379-f1ad-438b-b6d6-b5cd80261646" % "thefrylock"
r = requests.get(link)

print(r.text)