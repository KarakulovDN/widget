from typing import Union


def filter_by_state(state_list: list) -> Union[list]:
    """Функция, которая принимает список словарей и опционально значение для ключа
    state 'EXECUTED'
    """
    return [x for x in state_list if x.get('state') == 'EXECUTED']


def sort_by_date(date_list: list) -> Union[list]:
    """Функция сортировки списка по дате в обратном порядке"""
    return sorted(date_list, key=lambda k: k['date'], reverse=True)
