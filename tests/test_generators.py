from typing import Any

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator(card_number) -> Any:
    """Функция тестирует генератор номеров карт"""
    card_number = card_number_generator(1111111111111111, 1111111111111112)
    try:
        assert next(card_number) == "1111 1111 1111 1111"
        assert next(card_number) == "1111 1111 1111 1112"
    except StopIteration as e:
        print(e)


def test_transaction_descriptions(transaction_list: Any) -> Any:
    """Функция тестирует описание транзакций"""
    num = transaction_descriptions(transaction_list)
    assert next(num) == "Перевод организации"
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод со счета на счет"
    assert next(num) == "Перевод с карты на карту"


def test_filter_by_currency(transaction_list: Any, currency_usd: Any, currency_rub: Any, date_empy: Any) -> Any:
    """Функция тестирует фильтрацию списка операций по валюте 'code'"""
    try:
        assert next(filter_by_currency(transaction_list, "USD")) == currency_usd
        assert next(filter_by_currency(transaction_list, "RUB")) == currency_rub
        assert next(filter_by_currency(transaction_list, "")) == date_empy
    except StopIteration as e:
        print(e)
