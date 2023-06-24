from src.classes.abstract_classes import API
from utils.search_city_id import search_city_sj
import requests


class ApiSuperJob(API):
    """Класс для получения словаря с вакансиями с помощью API к SuperJob"""
    __slots__ = ['city', 'skills']

    def __init__(self, city: str, skills: str) -> None:
        """

        :param city: название города
        :param skills: список ключевых слов
        """
        self.city_id = search_city_sj(city)
        self.skills = skills

    def api_connect(self, headers: str = None) -> dict:
        """

        :param headers: ключ для работы с API
        :return: словарь с вакансиями полученным по API
        """
        response = requests.get("https://api.superjob.ru/2.0/vacancies/", headers={"X-Api-App-Id": headers},
                                params={"town": self.city_id, 'keyword': self.skills})
        return response.json()
