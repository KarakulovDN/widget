from typing import Any

from src.widget import get_date, mask_account_card


def test_mask_account_card(prefix_account_number: Any, prefix_visa_classic_card_number: Any,
                           prefix_mastercard_card_number: Any, card_number_empty: Any, account_number_empty: Any,
                           prefix_maestro_card_number: Any, prefix_visa_platinum_card_number: Any,
                           account_number_word: Any, prefix_visa_classic_card_number_empy: Any,
                           prefix_visa_incorrect: Any, account_number: Any) -> Any:
    assert mask_account_card(prefix_account_number) == 'Счет **4305'
    assert mask_account_card(prefix_visa_classic_card_number) == 'Visa Classic 6831 98** **** 7658'
    assert mask_account_card(prefix_mastercard_card_number) == 'MasterCard 7158 30** **** 6758'
    assert mask_account_card(card_number_empty) == 'Это поле не может быть пустым'
    assert mask_account_card(account_number_empty) == 'Это поле не может быть пустым'
    assert mask_account_card(prefix_maestro_card_number) == 'Maestro 1596 83** **** 5149'
    assert mask_account_card(prefix_visa_platinum_card_number) == 'Visa Platinum 8990 92** **** 5229'
    assert mask_account_card(account_number_word) == "Счет Поле \"Номер банковского счета\" не должно быть пустым"
    assert mask_account_card(prefix_visa_classic_card_number_empy) == "Поле \"Номер карты\" не должно быть пустым"
    assert mask_account_card(prefix_visa_incorrect) == 'Visa Plattinum 7158 30** **** 6758'
    assert mask_account_card(account_number) == 'Указаны не корректные данные'


def test_get_data(date_text: Any, date_contrary: Any, date_slash: Any, date_empy: Any, date_data: Any) -> Any:
    assert get_date(date_text) == "Неправильный формат даты"
    assert get_date(date_contrary) == "Неправильный формат даты"
    assert get_date(date_slash) == "Неправильный формат даты"
    assert get_date(date_empy) == "Поле \"Дата\" не должно быть пустым"
    assert get_date(date_data) == "11.03.2024"
