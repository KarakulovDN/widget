from typing import Any

import pytest


@pytest.fixture
def card_number() -> Any:
    return "1596837868705149"


@pytest.fixture
def card_number_empty() -> Any:
    return ""


@pytest.fixture
def account_number() -> Any:
    return "73654108430135874305"


@pytest.fixture
def account_number_empty() -> Any:
    return ""


@pytest.fixture
def prefix_visa_classic_card_number_empy() -> Any:
    return "Visa Classic"


@pytest.fixture
def prefix_visa_classic_card_number() -> Any:
    return "Visa Classic 6831982476737658"


@pytest.fixture
def prefix_visa_incorrect() -> Any:
    return "Visa Plattinum 7158300734726758"


@pytest.fixture
def prefix_account_number() -> Any:
    return "Счет 73654108430135874305"


@pytest.fixture
def prefix_mastercard_card_number() -> Any:
    return "MasterCard 7158300734726758"


@pytest.fixture
def prefix_maestro_card_number() -> Any:
    return "Maestro 1596837868705149"


@pytest.fixture
def prefix_visa_platinum_card_number() -> Any:
    return "Visa Platinum 8990922113665229"


@pytest.fixture
def card_number_letter() -> Any:
    return "899092t113665229"


@pytest.fixture
def card_number_word() -> Any:
    return "номер_карты"


@pytest.fixture
def account_number_word() -> Any:
    return "Счет номер_карты"


@pytest.fixture
def account_number_letter() -> Any:
    return "7365410y430135874305"


@pytest.fixture
def date_slash() -> Any:
    return "12/11/2025"


@pytest.fixture
def date_contrary() -> Any:
    return "2020.12.12"


@pytest.fixture
def date_data() -> Any:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def date_text() -> Any:
    return "dd.mm.YYYY"


@pytest.fixture
def date_empy() -> Any:
    return ""


@pytest.fixture
def transaction_list() -> Any:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
            {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}, },
            "description": "Перевод организации", "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702", },
        {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount":
            {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}, },
            "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188", },
        {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount":
            {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}, },
            "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160", },
        {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916", "operationAmount":
            {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}, },
            "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229", },
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "operationAmount":
            {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}, },
            "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657", },
    ]


@pytest.fixture
def currency_usd() -> Any:
    return {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
            {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}, },
            "description": "Перевод организации", "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702", }


@pytest.fixture
def currency_rub() -> Any:
    return {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount":
            {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}, },
            "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160", }
