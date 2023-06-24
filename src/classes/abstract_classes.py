from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def api_connect(self, all_vacancies):
        pass


class Saver(ABC):

    @classmethod
    @abstractmethod
    def load_vacancies_json(cls):
        pass

    @classmethod
    @abstractmethod
    def to_json(cls, all_vacancies):
        pass

    @classmethod
    @abstractmethod
    def del_vacancies(cls, index: int):
        pass
