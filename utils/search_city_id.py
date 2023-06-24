import os

import requests


def search_city_hh(city_find: str) -> str:
    """Подключается к API HH с id городов и ищет по названию города его id"""
    hh_areas_url = 'https://api.hh.ru/areas'
    response = requests.get(hh_areas_url)
    if response.status_code == 200:
        for country in response.json():
            for region in country['areas']:
                if region['name'].lower() == city_find.lower():
                    return region['id']
                for city in region['areas']:
                    if city['name'].lower() == city_find.lower():
                        return city['id']
    else:
        raise Exception(f'Ошибка при выполнении запроса: {response.status_code}')


def search_city_sj(city_find: str) -> str:
    """Подключается к API SJ с id городов и ищет по названию города его id"""
    sj_areas_url = "https://api.superjob.ru/2.0/towns/"
    x_api_app_id = os.getenv("X_API_APP_ID_KEY")
    response = requests.get(sj_areas_url, headers={"X-Api-App-Id": x_api_app_id})
    if response.status_code == 200:
        for city in response.json()['objects']:
            if city['title'].lower() == city_find.lower() or city['title_eng'].lower() == city_find.lower():
                return city['id']
    else:
        raise Exception(f'Ошибка при выполнении запроса: {response.status_code}')