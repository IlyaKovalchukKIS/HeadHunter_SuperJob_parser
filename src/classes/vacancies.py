class Vacancies:
    """Класс вакансий"""
    all_instance_vacancies = []
    all_list_vacancies = []
    __slots__ = ['__format_dict_vacancy', '__name', '__url', '__salary', '__description']

    def __init__(self, format_dict_vacancy: dict = None) -> None:
        """

        :param format_dict_vacancy: словарь вакансии
        """
        self.__name = format_dict_vacancy['name']  # название вакансии
        self.__url = format_dict_vacancy['url']  # ссылка на вакансию
        self.__salary = format_dict_vacancy['salary']  # зарплата вакансии
        self.__description = format_dict_vacancy['description']  # описание вакансии
        self.all_instance_vacancies.append(self)  # добавление экземпляров класса в список
        self.all_list_vacancies.append(format_dict_vacancy)  # добавление словаря вакансий в список

    def __str__(self) -> str:
        """

        :return: текстовое представление вакансии класса
        """
        salary_format = ''
        if self.__salary['from'] == 0 and self.__salary['to'] == 0:
            salary_format += 'Не указана'
        elif self.__salary['from'] == 0:
            salary_format += f"до {self.__salary['to']}"
        elif self.__salary['to'] == 0:
            salary_format += f"от {self.__salary['from']}"
        else:
            salary_format += f"от {self.__salary['from']} до {self.__salary['to']}"

        return f"Название: {self.__name}\n" \
               f"Зарплата: {salary_format}\n" \
               f"Краткое описание:\n" \
               f"{self.__description}...\n" \
               f"!Для полного отображения вакансии перейдите по ссылке! -> {self.__url}\n" \
               f"{'_' * 150}"

    @staticmethod
    def salary_comparison(vacancies_file: dict) -> list:
        """

        :param vacancies_file: словарь со всеми вакансиями
        :return: словарь отфильтрованных вакансий по максимальной зарплате
        """
        sort_vacancies = sorted(vacancies_file, key=lambda x: x.get('salary').get('to'), reverse=True)
        return sort_vacancies
