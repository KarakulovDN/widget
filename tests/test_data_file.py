from unittest.mock import Mock, mock_open, patch

from src.data_file import read_csv_file, read_excel_file


@patch("builtins.open", new_callable=mock_open,
       read_data='id;state;date;amount;currency_name\n4653427;PENDING;2020-10-04T12:12:23Z;34072;Yuan')
def test_read_csv(mock_file):
    """ Тест проверки считывания файла формата csv. """
    mock_csv_file = read_csv_file("../data/transactions.csv")
    converted_to_dict = [
        {"id": "4653427",
         "state": "PENDING",
         "date": "2020-10-04T12:12:23Z",
         "amount": "34072",
         "currency_name": "Yuan"}
    ]
    assert mock_csv_file == converted_to_dict


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_read_csv_empty(mock_file):
    """ Тест проверки считывания пустого файла формата csv. """
    mock_csv_file = read_csv_file("../data/transactions.csv")
    assert mock_csv_file == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_csv_no_file(mock_file):
    """ Тест на отсутствие файла формата csv. """
    mock_no_file = read_csv_file("../data/transactions.csv")
    assert mock_no_file == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_excel_no_file(mock_file):
    """ Тест на отсутствие файла формата excel. """
    mock_no_file = read_excel_file("../data/transactions_excel.xlsx")
    assert mock_no_file == []
