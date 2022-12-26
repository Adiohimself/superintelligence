import requests
import json

heroes_list = ['Hulk', 'Captain America', 'Thanos']

intelligence_dict = {}

url = 'https://akabab.github.io/superhero-api/api/all.json'

hero_list = json.loads(requests.get(url).content)
for hero in hero_list:
    for hero_in_my_dict in heroes_list:
        if hero_in_my_dict == hero['name']:
            name = hero['name']
            intelligence = hero['powerstats']['intelligence']
            intelligence_dict[name] = intelligence

print('самый умный супергерой из вашего списка:', max(intelligence_dict, key=intelligence_dict.get))

