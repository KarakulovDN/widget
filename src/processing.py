from typing import Any, Dict, List

# Список для проверки функций
user_id_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(user_id_list: dict[str, str | bool], state: str) -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    return [
        list_items for list_items in user_id_list if isinstance(list_items, dict) and list_items.get('state') == state
    ]


def sort_by_date(user_id_list: dict[str, str | bool], ascending: bool = True) -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отсортированный по дате (date)"""

    # Проверяем, что все элементы являются словарями и имеют ключ 'date'
    filtered_list = [k for k in user_id_list if isinstance(k, dict) and 'date' in k]

    # Сортируем по дате, убирая ошибку с типом
    return sorted(filtered_list, key=lambda k: k["date"][:10], reverse=not ascending)

# Проверка функций принтом
# print(user_id_list)
# print(sort_by_date(user_id_list))
# print(filter_by_state(user_id_list, state='EXECUTED'))
