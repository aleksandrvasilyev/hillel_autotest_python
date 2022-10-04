import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
astros = response.json()

for astro in astros['people']:
    print(astro['name'])
