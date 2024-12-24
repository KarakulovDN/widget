import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(filename)s: %(funcName)s (строка вызова %(lineno)s): %(asctime)s - %(message)s",
    filename="../logs/masks.log",
    encoding="utf-8",
    filemode="w",
)
get_operations_data_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()


def get_mask_card_number(card_number: str) -> Union[str]:
    """Функция маскировки номера банковской карты"""
    logging.info('Получаем данные карты')
    if card_number.isdigit() and len(card_number) == 16:
        hide_digital = card_number[6:-4]
        digital_stars = ""
        for digits in hide_digital:
            if digits >= '0':
                digital_stars += "*"
        card_number_hide = card_number[0:6] + digital_stars + card_number[-4:]
        card_number_split = ' '.join(card_number_hide[i * 4:(i + 1) * 4] for i in range(4))
        logging.info(f'Номер карты введен корректно {card_number_split}')
        return card_number_split
    # Проверка на пустую строку
    elif len(card_number) == 0:
        logging.info('Пустое поле номера карты')
        return "Поле \"Номер карты\" не должно быть пустым"
    else:
        logging.error('Не корректный номер карты')
        return "Введен не корректный номер карты"


def get_mask_account(mask_account: str) -> Union[str]:
    """Функция маскировки номера банковского счета"""
    logging.info('Получаем данные счета')
    if mask_account.isdigit() and len(mask_account) == 20:
        hide_digital = mask_account[:-4]
        digital_stars = ""
        for digits in hide_digital:
            if digits >= '0':
                digital_stars += "*"

        bank_account_hide = digital_stars + mask_account[-4:]
        logging.info(f'Номер банковского счета введен корректно {bank_account_hide}')
        return bank_account_hide[-6:]
    # Проверка на пустую строку
    elif len(mask_account) == 0:
        logging.info('Пустое поле номера банковского счета')
        return "Поле \"Номер банковского счета\" не должно быть пустым"

    else:
        logging.error('Не корректный номер банковского счета')
        return "Введен не корректный номер счета"


print(get_mask_card_number("1234567891234567"))
print(get_mask_card_number("123456789134567"))

print(get_mask_account("12345678911234567891"))
print(get_mask_account("1234567891234567"))
