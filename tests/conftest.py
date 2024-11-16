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
