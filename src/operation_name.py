import re
from collections import Counter

from src.utils import transaction


def bank_operation(list_dict: list[dict], search: str) -> list[dict]:
    """ Функция для поиска в списке словаре операций по заданной строке — описанию"""
    new_operation_list = []
    for transactions in list_dict:
        if "description" in transactions and re.search(search, transactions["description"], flags=re.IGNORECASE):
            new_operation_list.append(transactions)
    return new_operation_list


if __name__ == "__main__":
    search_op = input("Введите тип операции: ")
    result = bank_operation(transaction, search_op)
    print(result)


def counter_desc(list_dict: list[dict], operation: str | bool) -> dict[str, int]:
    """ Функция для подсчета количества банковских операций определенного типа"""
    new_list_counter = []
    for transactions in list_dict:
        if "description" in transactions and transactions["description"] in operation:
            new_list_counter.append(transactions)
    sort = Counter(operation).most_common()
    return dict(sort)


if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
        "Перевод с карты на счет",
        "Открытие вклада",
    ]

    print(counter_desc(transaction, categories_operations))
