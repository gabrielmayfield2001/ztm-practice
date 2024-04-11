import requests


def test_weather_response():
    api_key = '2c3a019243e8ebcfdc78aeb91f5aeb4c'
    city_name = 'Houston'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = f'{base_url}appid={api_key}&q={city_name}'
    response = requests.get(complete_url)
    data = response.json()

    assert response.status_code == 200
    assert 'weather' in data
    assert 'main' in data
    assert data['name'] == 'Houston'
