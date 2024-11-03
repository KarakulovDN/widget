from src.masks import get_mask_account, get_mask_card_number
from typing import Union

def get_date(current_data: str) -> Union[str]:
    """Функция определяющая текущую дату в формате dd.mm.YYYY"""
    return f"{current_data[8:10]}.{current_data[5:7]}.{current_data[:4]}"


def mask_account_card(string_bank_card_or_bank_account: str) -> Union[str]:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    account_bank = "".join("" if el.isdigit() else el for el in string_bank_card_or_bank_account)
    if 'Счет ' in string_bank_card_or_bank_account:
        number_account_mask = "".join(numbers if numbers.isdigit() else "" for numbers in string_bank_card_or_bank_account)
        return 'Счет ' + get_mask_account(number_account_mask)
    else:
        number_card = "".join(numbers if numbers.isdigit() else "" for numbers in string_bank_card_or_bank_account)
        number_card_mask = get_mask_card_number(number_card)
        name_card = "".join("" if el.isdigit() else el for el in string_bank_card_or_bank_account)
        data_card_mask = name_card + number_card_mask
        return data_card_mask
#
print(mask_account_card('Maestro 1596837868705199'))
# print(mask_account_card('Счет 64686473678894779589'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Счет 35383033474447895560'))
# print(mask_account_card('Visa Classic 6831982476737658'))
# print(mask_account_card('Visa Platinum 8990922113665229'))
# print(mask_account_card('Visa Gold 5999414228426353'))
# print(mask_account_card('Счет 73654108430135874305'))

# print(get_date('2024-03-11T02:26:18.671407'))
#






