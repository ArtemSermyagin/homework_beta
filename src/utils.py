import json

from json import JSONDecodeError
from typing import Any


def read_json(path: str) -> list[Any]:
    try:
        with open(path) as file:
            read = json.load(file)
            return read
    except JSONDecodeError:
        return []


def get_transaction(id_trans: int) -> Any:
    path_json = "../data/operations.json"
    data = read_json(path_json)
    for item in data:
        if item["id"] == id_trans and item["operationAmount"]["currency"]["code"] == "RUB":
            return float(item["operationAmount"]["amount"])
    raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")


# print(get_transaction(587085106))
# print(read_json('../data/operations.json'))
