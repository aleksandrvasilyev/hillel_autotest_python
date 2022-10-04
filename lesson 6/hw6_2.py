import requests

while True:
    # city = 'vinnytsia'
    city = input('Введите город (odesa, kyiv, lviv, kharkiv, vinnytsia): ')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
    response = requests.get(url)
    weather = response.json()

    print(f"Город - {city.capitalize()}, температура - {weather['main']['temp']}°C, скорость ветра - {weather['wind']['speed']} м./с.")

