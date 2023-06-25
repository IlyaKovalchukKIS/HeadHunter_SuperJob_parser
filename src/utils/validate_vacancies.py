import re


def validate_vacancies_hh(dict_vacancies: dict):
    """

    :param dict_vacancies: словарь вакансии полученный с сайта HeadHunter
    :return: форматированный словарь вакансии для работы с ним в классе Vacancies
    """
    name = ''
    url = ''
    salary = {'from': 0,
              'to': 0}
    description = ''

    if dict_vacancies['name'] is not None:
        name += dict_vacancies['name']
    if dict_vacancies['alternate_url'] is not None:
        url += dict_vacancies['alternate_url']
    if dict_vacancies['salary'] is not None:
        if dict_vacancies['salary']['from'] is None and dict_vacancies['salary']['to'] is None:
            salary['from'] = 0
        elif dict_vacancies['salary']['to'] is None:
            # salary += f"от {dict_vacancies['salary']['from']}"
            salary['from'] = dict_vacancies['salary']['from']
        elif dict_vacancies['salary']['from'] is None:
            # salary += f"до {dict_vacancies['salary']['to']}"
            salary['to'] = dict_vacancies['salary']['to']
        else:
            salary['from'] = dict_vacancies['salary']['from']
            salary['to'] = dict_vacancies['salary']['to']
            # salary += f"от {salary_from} до {salary_to}"

    if dict_vacancies['snippet']['responsibility'] is not None:
        text = dict_vacancies['snippet']['responsibility']
        cleaned_text = re.sub('</?highlighttext>', '', text)
        description += cleaned_text
    else:
        text = dict_vacancies['snippet']['requirement']
        cleaned_text = re.sub('</?highlighttext>', '', text)
        description += cleaned_text

    return vacancies_format(name, url, salary, description)


def validate_vacancies_sj(dict_vacancies):
    """

    :param dict_vacancies: словарь вакансии полученный с сайта SuperJob
    :return: форматированный словарь вакансии для работы с ним в классе Vacancies
    """
    name = ''
    url = ''
    salary = {'from': 0,
              'to': 0}
    description = ''

    if dict_vacancies['profession']:
        name += dict_vacancies['profession']
    if dict_vacancies['link']:
        url += dict_vacancies['link']
    if dict_vacancies['payment_from'] == 0 and dict_vacancies['payment_to'] == 0:
        salary['from'] = 0
    elif dict_vacancies['payment_to'] == 0:
        # salary += f"от {dict_vacancies['payment_from']}"
        salary['from'] = dict_vacancies['payment_from']
    elif dict_vacancies['payment_from'] == 0:
        # salary += f"до {dict_vacancies['payment_to']}"
        salary['to'] = dict_vacancies['payment_to']
    else:
        salary['from'] = dict_vacancies['payment_from']
        salary['to'] = dict_vacancies['payment_to']
        # salary += f"от {salary_from} до {salary_to}"
    if dict_vacancies['vacancyRichText']:
        clean_text = re.sub('/?\n', '', dict_vacancies['vacancyRichText'])
        regexp = re.compile('<.*?>')
        cleaned_string = re.sub(regexp, '', clean_text)
        description += cleaned_string

    return vacancies_format(name, url, salary, description)


def vacancies_format(name, url, salary, description):
    """

    :param name: название вакансии
    :param url: ссылка на вакансию
    :param salary: зарплата в вакансии
    :param description: описание вакансии
    :return: словарь отформатированной вакансии
    """
    vacancies = {'name': f"{name}",
                 'url': f"{url}",
                 'salary': salary,
                 'description': f"{description}"}
    return vacancies
