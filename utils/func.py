from engine_classes import HH, SuperJob
from vacancy import HHVacancy, SJVacancy


def check_search(hh: HH, sj: SuperJob) -> bool:
    """Проверяет наличие вакансий на HeadHunter и SuperJob.

    Args:
        hh (HH): Экземпляр класса HH.
        sj (SuperJob): Экземпляр класса SuperJob.

    Returns:
        bool: True, если есть вакансии, иначе False.
    """
    hh_items = hh.get_request().get('items', [])
    sj_objects = sj.get_request().get('objects', [])
    return bool(hh_items or sj_objects)


def get_vacancies(data):
    """Возвращает список всех вакансий для экземпляров классов HHVacancy и SJVacancy.

    Args:
        data (list): Список словарей с данными о вакансиях.

    Returns:
        list: Список экземпляров классов HHVacancy и SJVacancy.
    """
    vacancies = []
    for item in data:
        if item['from'] == 'HeadHunter':
            vacancies.append(HHVacancy(item))
        else:
            vacancies.append(SJVacancy(item))
    return vacancies


def get_top_vacancies(vacancies, top_count=5, sort_key='max_salary'):
    """Возвращает топ вакансий, отсортированных по указанному ключу.

    Args:
        vacancies (list): Список экземпляров классов HHVacancy и SJVacancy.
        top_count (int): Количество вакансий в топе (по умолчанию 5).
        sort_key (str): Ключ сортировки ('max_salary' или 'date_published').

    Returns:
        list: Топ вакансий, отсортированных по указанному ключу.
    """
    if sort_key == 'max_salary':
        sort_func = lambda vacancy: vacancy.max_salary
        reverse = True
    elif sort_key == 'date_published':
        sort_func = lambda vacancy: vacancy.Vacancy.date_published
        reverse = False
    else:
        raise ValueError(f"Некорректный ключ сортировки '{sort_key}'")
    return sorted(vacancies, key=sort_func, reverse=reverse)[:top_count]
