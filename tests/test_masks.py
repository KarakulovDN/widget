from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def test_account_number(account_number: Any, account_number_word: Any, account_number_empty: Any,
                        account_number_letter: Any) -> Any:
    assert get_mask_account(account_number) == "**4305"
    assert get_mask_account(account_number_word) == "Введен не корректный номер счета"
    assert get_mask_account(account_number_empty) == "Поле \"Номер банковского счета\" не должно быть пустым"
    assert get_mask_account(account_number_letter) == "Введен не корректный номер счета"


def test_mask_card_number(card_number: Any, card_number_empty: Any, card_number_word: Any,
                          card_number_letter: Any) -> Any:
    assert get_mask_card_number(card_number) == "1596 83** **** 5149"
    assert get_mask_card_number(card_number_empty) == "Поле \"Номер карты\" не должно быть пустым"
    assert get_mask_card_number(card_number_word) == "Введен не корректный номер карты"
    assert get_mask_card_number(card_number_letter) == "Введен не корректный номер карты"
