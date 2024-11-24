import re
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def get_date(current_data: str) -> Union[str]:
    """Функция определяющая текущую дату в формате dd.mm.YYYY"""
    # Проверка на пустую строку
    if len(current_data) == 0:
        return "Поле \"Дата\" не должно быть пустым"

    # Проверка формата даты с временем
    pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?$'
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
            number_card_mask = get_mask_card_number(number_card)
            name_cards = "".join("" if el.isdigit() else el for el in string_bank_card_or_bank_account)
            # Список платёжных систем
            all_name_card = ["Visa ", "Visa Classic ", "Visa Gold ", "Visa Platinum ", "Maestro ",
                             "MasterCard ", "Мир ", "Счет "]
            if name_cards in all_name_card:
                return name_cards + number_card_mask
            else:
                return "Платёжная система не найдена"

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
# print(mask_account_card('Visa Gold'))
# print(mask_account_card('Visa Plattinum 7158300734726758'))
# print(mask_account_card('73654108430135874305'))
