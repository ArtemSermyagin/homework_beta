import json

from json import JSONDecodeError


def read_json(path: str) -> list[dict]:
    try:
        with open(path) as file:
            read = json.load(file)
            return read
    except JSONDecodeError:
        return []


def get_transaction(id_trans):
    path_json = '../data/operations.json'
    data = read_json(path_json)
    for item in data:
        if item['id'] == id_trans and item['operationAmount']["currency"]['code'] == "RUB":
            return item['operationAmount']['amount']
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")



print(get_transaction(41428829))
# print(read_json('../data/operations.json'))
