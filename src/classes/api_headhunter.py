from abstract_classes import API
from utils.search_city_id import search_city_hh
import requests


class ApiHeadHunter(API):
    """Класс для подключения по API к HeadHunter"""
    __slots__ = ['city', 'skills']

    def __init__(self, city: str, skills: str) -> None:
        """

        :param city: id города
        :param skills: список ключевых слов
        """
        self.params = self.parameters_dict(search_city_hh(city), skills)

    @staticmethod
    def parameters_dict(city: str, skills: str) -> dict:
        profession_list = skills.split(' ')
        if len(profession_list) > 1:
            skills = " AND ".join([f"\"{skill}\"" for skill in profession_list])
        else:
            skills = skills
        parameters = {
            'text': skills,
            'area': search_city_hh(city)
        }
        return parameters

    def api_connect(self, headers: str = None) -> list:
        """

        :param headers: ключ для работы с API
        :return: словарь с вакансиями полученным по API
        """
        response = requests.get("https://api.hh.ru/vacancies", params=self.params, headers=headers)
        return response.json()
