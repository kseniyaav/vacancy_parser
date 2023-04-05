import json
import os


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в формате JSON.
    """
    def __init__(self, file_path: str):
        """
        Инициализация коннектора к файлу.

        :param file_path: путь к файлу с данными.
        """
        self.__data_file = file_path
        self.__connect()

    @property
    def data_file(self):
        """
        Возвращает текущий путь к файлу с данными.
        """
        return self.__data_file

    @data_file.setter
    def data_file(self, value: str):
        """
        Изменяет путь к файлу с данными.

        :param value: новый путь к файлу с данными.
        """
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
        Проверяет существование файла с данными и создает его, если необходимо.
        """
        if not os.path.isfile(self.__data_file):
            raise FileNotFoundError(f"Файл {self.__data_file} не найден.")
        with open(self.__data_file, 'r', encoding="utf8") as file:
            json_reader = json.load(file)
            if not isinstance(json_reader, list):
                raise Exception('Файл должен содержать список')

    def insert(self, path: str, data: list):
        """
        Записывает данные в файл с сохранением структуры и исходных данных.

        :param path: путь к файлу для записи.
        :param data: данные для записи в файл.
        """
        with open(path, 'w', encoding="UTF-8") as file:
            json.dump([e.to_dict() for e in data], file, indent=4, ensure_ascii=False, skipkeys=True, sort_keys=True)

    def select(self, query: dict):
        """
        Выбирает данные из файла с применением фильтрации.

        :param query: словарь с параметрами фильтрации.
                      Ключ - поле для фильтрации, значение - искомое значение.
        :return: отфильтрованные данные из файла.
        """
        result = []
        with open(self.__data_file, 'r', encoding="UTF-8") as file:
            data = json.load(file)

        if not query:
            return data

        for item in data:
            for key, value in query.items():
                if item.get(key) == value:
                    result.append(item)

        return result
