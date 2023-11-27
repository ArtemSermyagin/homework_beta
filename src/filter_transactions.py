import re
from collections import Counter


def filter_transactions(operations: list[dict[str, str]], search_text: str) -> list[list[dict[str, str]]]:
    """
    Фильтрует транзакции по условию
    :param operations: Список словарей с транзакциями
    :param search_text: Условие поиска
    :return: список операций
    """
    return [operations for operation in operations if
            re.search(search_text, operation.get("description", ""), re.IGNORECASE)]


def count_operations(operations: list[dict[str, str]], categories: dict[str, str]) -> Counter:
    """
    Считает количество операций по категориям
    :param operations: Список операций
    :param categories: Словарь с категориями операций
    :return: Счетчик операций разбитый по категориям
    """
    return Counter(
        operation.get("category", "") for operation in operations if operation.get("category", "") in categories)
