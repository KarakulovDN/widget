import re
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def get_date(current_data: str) -> Union[str]:
    """Функция определяющая текущую дату в формате dd.mm.YYYY"""
    # Проверка на пустую строку
    if len(current_data) == 0:
        return "Поле \"Дата\" не должно быть пустым"
    # Проверка формата даты с временем
    pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?$'
    if not re.match(pattern, current_data):
        return "Неправильный формат даты"
    # Извлечение даты
    date_part = current_data.split('T')[0]
    year, month, day = date_part.split('-')
    # Проверка на содержимое букв
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return "Должны быть только цифры"

    return f"{day}.{month}.{year}"


def mask_account_card(string_bank_card_or_bank_account: str) -> Union[str]:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    # Проверка на пустую строку
    if len(string_bank_card_or_bank_account) == 0:
        return "Это поле не может быть пустым"
    elif 'Счет ' in string_bank_card_or_bank_account:
        number_account_mask = "".join(num if num.isdigit() else "" for num in string_bank_card_or_bank_account)
        return 'Счет ' + get_mask_account(number_account_mask)
    else:
        number_card = "".join(numbers if numbers.isdigit() else "" for numbers in string_bank_card_or_bank_account)
        # Проверка на пустую строку
        if len(number_card) == 0:
            return "Поле \"Номер карты\" не должно быть пустым"
        if len(number_card) == 16:
            name_cards = "".join("" if el.isdigit() else el for el in string_bank_card_or_bank_account)
            # Парсинг платёжных систем и номера счета/карты
            name_cards = re.match(r'([A-Za-zА-Яа-яЁё\s]+)(\d+)?', string_bank_card_or_bank_account.strip())
            if name_cards:
                # Если совпадение найдено, возвращаем слова и числа
                words = name_cards.group(1).strip()
                numbers = name_cards.group(2) if name_cards.group(2) else 'Номер карты / счета не найден'
                return words + ' ' + get_mask_card_number(numbers)
            else:
                return "Нет информации о карте"

    return "Указаны не корректные данные"


# print(mask_account_card('Maestro 1596837868705149'))
# print(mask_account_card('Счет 64686473678894779589'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Счет 35383033474447895560'))
# print(mask_account_card('Visa Classic 6831982476737658'))
# print(mask_account_card('Visa Platinum 8990922113665229'))
# print(mask_account_card('Visa Gold 5999414228426353'))
# print(mask_account_card('Счет 73654108430135874305'))
# print(get_date('2024-03-11T02:26:18.671407'))
# print(get_date('2020-10-07T08:49:52Z'))
# print(mask_account_card('Visa Gold'))
# print(mask_account_card('Visa Plattinum 7158300734726758'))
# print(mask_account_card('73654108430135874305'))
# print(mask_account_card('Visa 4485542637612146'))
# print(mask_account_card('4485542637612146'))
# print(mask_account_card('Visa Gold 5999414228426353'))
# print(mask_account_card('Visa Gold 5999414228426353'))
