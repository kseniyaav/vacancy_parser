import os
from utils.engine_classes import Engine, HH, SuperJob
from func import check_search, get_vacancies, get_top_vacancies


def main():
    path = os.path.join('data.json')
    connector = Engine.get_connector(path)

    search_keyword = input('Введите ключевое слово поиска')

    hh = HH(search_keyword)
    sj = SuperJob(search_keyword)
    if check_search(hh, sj):
        h = hh.vacancies
        s = sj.vacancies
        all_vacancies = h + s
        connector.insert(path, all_vacancies)

    top_count = input('Введите колличество выводимых на экран вакансий')
    if not top_count.isdigit() or int(top_count) <= 0:
        print('Введите число больше 0')

    else:
        top_count = int(top_count)


if __name__ == '__main__':
    main()
