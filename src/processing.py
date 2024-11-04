def filter_by_state(state_list: list[dict[str]]) -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа
    state 'EXECUTED'
    """
    return [x for x in state_list if x.get('state') == 'EXECUTED']


def sort_by_date(date_list: list[dict[str]]) -> list:
    """Функция сортировки списка по дате в обратном порядке"""
    return sorted(date_list, key=lambda k: k['date'], reverse=True)


test_sort = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(test_sort)
print(sort_by_date(test_sort))
print(filter_by_state(test_sort))
