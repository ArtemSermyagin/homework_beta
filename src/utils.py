import json

from json import JSONDecodeError
from typing import Any


def read_json(path: str) -> list[Any]:
    """
    Принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    :param path: Путь к файлу
    :return: Список словарей с данными о финансовых транзакциях или пустой список
    """
    try:
        with open(path) as file:
            read = json.load(file)
            return read
    except JSONDecodeError:
        return []
    except FileNotFoundError:
        return []


def get_transaction(trans: dict) -> Any:
    """
    Функция возвращает сумму транзации, при условии совершения транзации в рублях
    :param trans: dict
    :return: float or Any
    """
    # path_json = "../data/operations.json"
    # data = read_json(path_json)
    # for item in data:
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        return float(trans["operationAmount"]["amount"])
    raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")


# print(get_transaction(587085106))
print(read_json('../data/operations.json'))
