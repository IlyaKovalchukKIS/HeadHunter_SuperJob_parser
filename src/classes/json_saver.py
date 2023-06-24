import json
import os

from abstract_classes import Saver


class JsonSaver(Saver):
    """Класс для подключения по API к SuperJob"""
    dir_path = os.path.abspath('vacancies_file/vacancies.json')

    @classmethod
    def load_vacancies_json(cls) -> dict:
        """Метод для загрузки вакансий из файла JSON"""
        with open(cls.dir_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @classmethod
    def to_json(cls, all_vacancies: list) -> None:
        """Метод для сохранения вакансий в файл"""
        with open(cls.dir_path, 'w', encoding='UTF-8') as f:
            json.dump(all_vacancies, f, indent=4, ensure_ascii=False)

    @classmethod
    def del_vacancies(cls, index: int) -> None:
        """Метод для удаления вакансий из файла"""
        with open(cls.dir_path, 'r') as f:
            vacancies = json.load(f)
        del vacancies[int(index) - 1]

        with open(cls.dir_path, 'w') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)
