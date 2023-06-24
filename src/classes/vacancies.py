class Vacancies:
    """Класс вакансий"""
    all_instance_vacancies = []
    __slots__ = ['format_dict_vacancy', '__name', '__url', '__salary', '__description']

    def __init__(self, format_dict_vacancy: dict) -> None:
        self.format_dict_vacancy = format_dict_vacancy
        self.__name = self.format_dict_vacancy['name']
        self.__url = self.format_dict_vacancy['url']
        self.__salary = self.format_dict_vacancy['salary']
        self.__description = self.format_dict_vacancy['description']

    def __str__(self) -> str:
        return f"Название: {self.__name}\n" \
               f"Зарплата: {self.__salary}\n" \
               f"Краткое описание:\n" \
               f"{self.__description}...\n" \
               f"!Для полного отображения вакансии перейдите по ссылке! -> {self.__url}\n" \
               f"{'_'* 150}"

    @staticmethod
    def salary_comparison(vacancies_file: list) -> list:
        sort_vacancies = sorted(vacancies_file, key=lambda x: x['salary'], reverse=True)
        return sort_vacancies
