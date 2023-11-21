import json

import pandas as pd

from settings import OPEN_TRANSACTIONS_CSV, DATA_PATH_2, TEST_DECOR_PATH, OPEN_TRANSACTIONS_XLSX


def transactions_open(path):
    try:
        transactions = pd.read_csv(path, error_bad_lines=False)
        return transactions.head()
    except TypeError:
        return "Файл не найден"


def transactions_xlsx_open(path):
    try:
        transactions_excel = pd.read_excel(path)
        return transactions_excel.head()
    except ValueError:
        return "Ошибка чтения файла excel"

# with open("../data/operations.json", encoding="utf-8") as f:
#     operations = json.load(f)
#     print(operations)
print(transactions_xlsx_open(OPEN_TRANSACTIONS_XLSX))