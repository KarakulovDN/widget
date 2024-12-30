from src.operation_name import bank_operation, counter_desc


def test_filter_by_description(dict_list_description):
    assert bank_operation(dict_list_description, 'Перевод') == [{'id': 41428829,
                                                                 'state': 'EXECUTED',
                                                                 'date': '2019-07-03T18:35:29.512364',
                                                                 'description': 'Перевод'},
                                                                {'id': 594226727, 'state': 'CANCELED',
                                                                 'date': '2018-09-12T21:27:25.241689',
                                                                 'description': 'Перевод'}]


def test_filter_description_empy(dict_list_description):
    assert bank_operation(dict_list_description, "Пополнение") == []


def test_counter_description(dict_list_description):
    assert (counter_desc(dict_list_description, ["Перевод", "Платеж", "Пополнение"])
            == {"Перевод": 1, "Платеж": 1, 'Пополнение': 1})
