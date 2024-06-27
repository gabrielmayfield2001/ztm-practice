import requests

api_key = '2c3a019243e8ebcfdc78aeb91f5aeb4c'

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = 'Houston'

complete_url = f"{base_url}appid={api_key}&q={city_name}"

response = requests.get(complete_url)

if __name__ == '__main__':
    if response.status_code == 200:
        print('successful')
        data = response.json()

        # Output

        if 'weather' in data and 'main' in data and 'name' in data:
            print(f'Weather data for the city of {data['name']}')
            print(f'Condition: {data['weather'][0]['description']}')
            print(f'Temperature: {data['main']['temp']} Kelvin')
            print(f'Pressure: {data['main']['pressure']} hPa')
            print(f'Humidity: {data['main']['humidity']}%')

        else:
            print('Some expected data is missing in the response')
    else:
        print('API request was unsuccessful')
