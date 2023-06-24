from pprint import pprint

from src.classes.api_superjob import ApiSuperJob
from src.classes.api_headhunter import ApiHeadHunter
from src.classes.json_saver import JsonSaver
from src.classes.vacancies import Vacancies
from utils.validate_vacancies import validate_vacancies_hh, validate_vacancies_sj, vacancies_format
import os

if __name__ == '__main__':
    api_key_sj = os.getenv("X_API_APP_ID_KEY")

    city = input('Для завершения работы с программой введите "exit"'
                 '\nВведите город для поиска вакансии\n'  # город для поиска вакансий
                 '>>> ')

    if city.lower() == 'exit':
        exit()

    keywords = input('Введите ключевое слово для поиска вакансии -\n'  # ключевые слова для поиска вакансий
                     'либо несколько через пробел\n'
                     '>>> ')

    if keywords.lower() == 'exit':
        exit()

    response_hh = ApiHeadHunter(city, keywords).api_connect()  # подключение к API HH
    for vacancy in response_hh['items']:
        vacancies_format_hh = validate_vacancies_hh(vacancy)  # валидация и форматирование вакансий по образцу
        Vacancies(vacancies_format_hh)  # инициализация класса вакансий

    response_sj = ApiSuperJob(city, keywords).api_connect(api_key_sj)  # подключение к API SJ
    for vacancy in response_sj['objects']:
        vacancies_format_sj = validate_vacancies_sj(vacancy)  # валидация и форматирование вакансий по образцу
        Vacancies(vacancies_format_sj)  # инициализация класса вакансий

    JsonSaver.to_json(Vacancies.all_list_vacancies)  # сохранение списка вакансий хранящихся в классе Vacancies

    user_input = ''
    while user_input.lower() != 'exit':
        user_input = input('1 - отобразить вакансии\n'
                           '2 - удалить вакансии\n'
                           '3 - отфильтровать вакансии по наибольшей зарплате\n'
                           '>>> ')

        if user_input == '1':
            for index, vacancy in enumerate(Vacancies.all_instance_vacancies):
                print(f"{index + 1}\n{vacancy}")

        if user_input == '2':
            user_input = input('Введите номер вакансии которую хотите удалить\n'
                               '>>> ')
            JsonSaver.del_vacancies(index=int(user_input))  # удаление вакансии по индексу
            load_vacancies = JsonSaver.load_vacancies_json()  # загрузка вакансий из файла после удаления
            Vacancies.all_instance_vacancies.clear()  # отчистка списка с вакансиями
            Vacancies.all_list_vacancies.clear()  # отчистка списка экземпляров класса вакансий
            for vacancy in load_vacancies:
                Vacancies(vacancy)  # создание новых списков с экземплярами и вакансиями после удаления

        if user_input == '3':
            load_vacancies = JsonSaver.load_vacancies_json()  # загрузка вакансий из файла json
            filter_salary = Vacancies.salary_comparison(load_vacancies)  # фильтрация вакансий по зарплате
            Vacancies.all_instance_vacancies.clear()  # отчистка списка с вакансиями
            Vacancies.all_list_vacancies.clear()  # отчистка списка экземпляров класса вакансий
            for vacancy in filter_salary:
                Vacancies(vacancy)  # создание новых списков с экземплярами и вакансиями после фильтрации по зарплате
