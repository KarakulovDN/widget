from typing import Any
from unittest.mock import patch

from src.external_api import convert_from_i_to_rub


@patch("requests.get")
def test_get_transaction_amount_in_rubles_rub(mock_get: Any) -> Any:
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    assert convert_from_i_to_rub(transaction) == 100


@patch("requests.get")
def test_get_transaction_amount_in_rubles_usd(mock_get: Any) -> Any:
    transaction = {"operationAmount": {"amount": 50, "currency": {"code": "USD"}}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 4340.0814}
    assert convert_from_i_to_rub(transaction) == 4340.0814


@patch("requests.get")
def test_get_transaction_amount_in_rubles_eur(mock_get: Any) -> Any:
    transaction = {"operationAmount": {"amount": 150, "currency": {"code": "EUR"}}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 13974.2193}
    assert convert_from_i_to_rub(transaction) == 13974.2193
