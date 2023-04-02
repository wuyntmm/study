import requests
import random

list_url = ["https://www.google.com/", "https://www.facebook.com/", "https://www.twitter.com/",
            "https://www.amazon.com/", "https://www.apple.com/"]

link = random.choice(list_url)

res = requests.get(link)
print(f'Status code is {res.status_code} from {link} with length of {len(res.text)} symbols')

# Task2

weather_link = "https://geocoding-api.open-meteo.com/v1/search?name="

city = input('Enter your city: ')

res2 = requests.get(f'{weather_link}{city}&count=1')

if len(res2.json()) - 1:
    data = res2.json()
    data2 = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude='
                         f'{data["results"][0]["latitude"]}&longitude={data["results"][0]["longitude"]}'
                         f'&current_weather=true').json()
    print(f"Current temperature in {city} is {data2['current_weather']['temperature']}")
else:
    print(f'There no such city as {city}')

