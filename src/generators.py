from typing import Iterator


def filter_by_currency(transactions: list[dict], code: str = "USD") -> Iterator:
    """Функция фильтрует словари по указанной валюте, по умолчанию это USD"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Функция отображает тип совершенной операции"""
    if len(transactions) > 0:
        for description in transactions:
            yield description["description"]


def card_number_generator(start: int, stop: int):
    """Функция генерирует номер карты"""
    if start < stop:
        for number in range(start, stop):
            card_numb = str(number)
            while len(card_numb) < 16:
                card_numb = '0' + card_numb
            yield f"{card_numb[:4]} {card_numb[4:8]} {card_numb[8:12]} {card_numb[12:]}"
