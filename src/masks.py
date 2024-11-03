def get_mask_card_number(card_number: [int]) -> [int]:
    """Функция маскировки номера банковской карты"""
    if card_number.isdigit() and len(card_number) == 16:
        hide_digital = card_number[6:-4]
        digital_stars = ""
        for digits in hide_digital:
            if digits >= '0':
                digital_stars += "*"

        card_number_hide = card_number[0:6] + digital_stars + card_number[-4:]
        card_number_split = ' '.join(card_number_hide[i * 4:(i + 1) * 4] for i in range(4))
        return card_number_split

    else:
        return "Введен не корректный номер карты"


def get_mask_account(mask_account: [int]) -> [int]:
    """Функция маскировки номера банковского счета"""
    if mask_account.isdigit() and len(mask_account) == 20:
        hide_digital = mask_account[:-4]
        digital_stars = ""
        for digits in hide_digital:
            if digits >= '0':
                digital_stars += "*"

        bank_account_hide = digital_stars + mask_account[-4:]
        return bank_account_hide[-6:]

    else:
        return "Введен не корректный номер счета"

#
# card_number_enter = "7000795649606361"
# print(get_mask_card_number(card_number_enter))


# bank_account = "73654108430135874305"
# print(get_mask_account(bank_account))
#