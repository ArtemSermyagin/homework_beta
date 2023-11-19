import json

from json import JSONDecodeError
from typing import Any

from src.log import log_utils


# from src.log import logger_1
log_1 = log_utils()


def read_json(path: str) -> Any:
    """
    Принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    :param path: str
    :return: Any
    """
    try:
        with open(path, encoding="utf-8") as file:
            read = json.load(file)
            # log = log_utils()
            log_1.info("Данные загружены")
            return read
    except JSONDecodeError:
        # log = log_utils()
        log_1.error("Ошибка чтения")
        return []
    except FileNotFoundError:
        # log = log_utils()
        log_1.error("Файл не найден")
        return []


def get_transaction(trans: dict) -> Any:
    """
    Функция возвращает сумму транзакции, при условии совершения транзакции в рублях
    :param trans: dict
    :return: float or Any
    """
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        # log = log_utils()
        log_1.info("Сумма транзакции выполненной в рублях.")
        return float(trans["operationAmount"]["amount"])
    # log = log_utils()
    log_1.error("Транзакция выполнена не в рублях.")
    raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")


print(get_transaction({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}))
print(read_json("../data/operations.json"))
