import csv

import pandas as pd


def transactions_open(path):
    """
    Функция считывает файлы csv
    :param path: path
    :return: list
    """
    try:
        transactions = []
        with open(path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                transactions.append(row)
        return transactions
    except TypeError:
        return "Файл не найден"


def transactions_xlsx_open(path):
    """
    Функция считывает файлы excel
    :param path: path
    :return: dict
    """
    try:
        transactions_excel = pd.read_excel(path)
        return transactions_excel.to_dict("records")
    except ValueError:
        return "Ошибка чтения файла excel"


# print(transactions_open(OPEN_TRANSACTIONS_CSV))
# print(transactions_xlsx_open(OPEN_TRANSACTIONS_XLSX))
