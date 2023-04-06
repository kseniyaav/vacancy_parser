import os
from utils.engine_classes import Engine, HH, SuperJob
from utils.func import check_search, get_vacancies, get_top_vacancies


def main():
    path = os.path.join('data.json')
    connector = Engine.get_connector(path)

    search_keyword = input('Введите ключевое слово поиска: ')

    hh = HH(search_keyword)
    sj = SuperJob(search_keyword)
    if check_search(hh, sj):
        h = get_vacancies(hh)
        s = get_vacancies(sj)
        all_vacancies = h + s
        connector.insert(path, all_vacancies)

    top_count = input('Введите количество выводимых на экран вакансий: ')
    if not top_count.isdigit() or int(top_count) <= 0:
        print('Введите число больше 0')

    else:
        top_count = int(top_count)
        vacancies = connector.select(path)
        top_vacancies = get_top_vacancies(vacancies, top_count)
        for vacancy in top_vacancies:
            print(vacancy)


if __name__ == '__main__':
    main()
