import json
import os

from abstract_classes import Saver


class JsonSaver(Saver):
    """Класс для подключения по API к SuperJob"""
    list_vacancies = []
    dir_path = os.path.abspath('vacancies_file/vacancies.json')

    def __init__(self, vacancy: dict):
        self.list_vacancies.append(vacancy)

    def to_json(self) -> None:
        """Метод для сохранения вакансий в файл"""
        with open(self.dir_path, 'w', encoding='UTF-8') as f:
            json.dump(self.list_vacancies, f, indent=4, ensure_ascii=False)

    def del_vacancies(self, index: int) -> None:
        """Метод для удаления вакансий из файла"""
        with open(self.dir_path, 'r') as f:
            vacancies = json.load(f)
        del vacancies[int(index) - 1]

        with open(self.dir_path, 'w') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)
