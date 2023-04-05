import datetime


class Vacancy:
    """
    Базовый класс для работы с вакансиями.
    """

    def __init__(self, name='', url='', description='', salary='', date_published=datetime.datetime.now(), **kwargs):
        """
        Создает новый экземпляр вакансии.

        :param name: название вакансии
        :param url: ссылка на вакансию
        :param description: описание вакансии
        :param salary: зарплата
        :param date_published: дата публикации вакансии
        """
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary
        self.date_published = date_published

    def __lt__(self, other):
        """
        Метод, который определяет порядок сортировки вакансий.

        :param other: другая вакансия, с которой сравнивается текущая
        :return: результат сравнения даты публикации вакансий
        """
        return self.date_published < other.date_published

    def __str_and_repr__(self):
        """
        Метод, который возвращает строковое представление объекта вакансии.

        :return: строковое представление вакансии
        """
        return f"{self.__class__.__name__}: {self.name}, зарплата: {self.salary} руб/мес"

    def to_dict(self):
        """
        Метод, который возвращает словарь с данными вакансии.

        :return: словарь с данными вакансии
        """
        return {
            'url': self.url,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'date_published': self.date_published
        }


class HHVacancy(Vacancy):
    """
    Класс, описывающий вакансию с сайта HeadHunter.
    """

    def __repr__(self):
        """
        Возвращает строковое представление объекта в формате:
        HH: {название вакансии}, зарплата: {зарплата} руб/мес ;
        """
        return f"HH: {self.name}, зарплата: {self.salary} руб/мес ;"

    def __str__(self):
        """
        Возвращает строковое представление объекта в формате:
        HH: {название вакансии}, зарплата: {зарплата} руб/мес ;
        """
        return f'HH: {self.name}, зарплата: {self.salary} руб/мес ;'

    @property
    def max_salary(self):
        """
        Возвращает максимальную зарплату вакансии. Если зарплата не указана,
        возвращает 0.
        """
        value = self.salary.get('to', 0)
        return 0 if value is None else value

    def __gt__(self, other):
        """
        Определяет оператор ">" для объектов класса.
        Возвращает True, если дата публикации вакансии self позже даты
        публикации other.
        """
        return self.date_published > other.date_published

    @property
    def datetime(self):
        """
        Возвращает дату публикации вакансии.
        """
        value = self.date_published
        return value


class SJVacancy(Vacancy):
    """
    Класс, описывающий вакансию с сайта SuperJob.
    """

    def __repr__(self):
        """Возвращает строковое представление вакансии на SuperJob."""
        return f"SJ: {self.name}, зарплата: {self.salary} руб/мес \n;"

    def __str__(self):
        """Возвращает строковое представление вакансии на SuperJob."""
        return f'SJ: {self.name}, зарплата: {self.salary} руб/мес \n;'

    @property
    def max_salary(self):
        """Возвращает максимальную зарплату вакансии на SuperJob."""
        value = self.salary
        return 0 if value is None else value

    def __gt__(self, other):
        """Определяет, какую вакансию на SuperJob считать более свежей."""
        return self.date_published > other.date_published

    @property
    def datetime(self):
        """Возвращает дату публикации вакансии на SuperJob."""
        value = self.date_published
        return value
