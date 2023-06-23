from abc import ABC, abstractmethod


class API(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def api_connect(self):
        pass


class Saver(ABC):

    @abstractmethod
    def to_json(self):
        pass

    @abstractmethod
    def del_vacancies(self, index: int):
        pass
