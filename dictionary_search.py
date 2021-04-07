import requests
import json


word = str(input("Word? <user inputs a word>(Ex – \“House\”)"))

url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US' + '/' + word.lower()

r = requests.get(url)
data = json.dumps(r.json())
print(data)



