from abstract_classes import Saver


class JsonSaver(Saver):
    """Класс для подключения по API к SuperJob"""

    def to_json(self, vacancies: list) -> None:
        """Метод для сохранения вакансий в файл"""
        pass

    def del_vacancies(self, index: int, vacancies: list) -> list:
        pass
