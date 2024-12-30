from src.data_file import read_csv_file, read_excel_file
from src.operation_name import bank_operation
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions_dictionary
from src.widget import get_date, mask_account_card


def main() -> None:
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.""")
    while True:
        print("Выберите необходимый файл:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        user_answer = input().strip()
        if user_answer == "1":
            print("Для обработки выбран JSON-файл.")
            list_transactions = get_transactions_dictionary("data/operations.json")
            break
        elif user_answer == "2":
            print("Для обработки выбран CSV-файл.")
            list_transactions = read_csv_file("data/transactions.csv")
            break
        elif user_answer == "3":
            print("Для обработки выбран XLSX-файл.")
            list_transactions = read_excel_file("data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный выбор.")
            continue

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_for_filter = input().upper()
        status_for_filter = status_for_filter.upper()
        if status_for_filter == "EXECUTED" or status_for_filter == "CANCELED" or status_for_filter == "PENDING":
            print(f"Операции отфильтрованы по статусу {status_for_filter}")
            break
        else:
            print(f"Статус операции {status_for_filter} недоступен")
    transaction_list = filter_by_state(list_transactions, status_for_filter)

    while True:
        sort_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if sort_date == "да":
            while True:
                sorted_operation = input("Отсортировать по возрастанию или по убыванию?\n"
                                         "1 - по возрастанию\n2 - по убыванию\n").lower()
                if sorted_operation == "по возрастанию" or sorted_operation == "1":
                    transaction_list = sort_by_date(transaction_list, ascending=False)
                    break
                elif sorted_operation == "по убыванию" or sorted_operation == "2":
                    transaction_list = sort_by_date(transaction_list, ascending=True)
                    break
                else:
                    print("Некорректный выбор.")
                    continue
            break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный выбор.")
            continue

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        answer_for_currency = input().lower()
        if answer_for_currency == "да":
            support_list = []
            if user_answer == "1":
                for transaction in transaction_list:
                    if transaction["operationAmount"]["currency"]["code"] == "RUB":
                        support_list.append(transaction)
            else:
                for transaction in transaction_list:
                    if transaction["currency_code"] == "RUB":
                        support_list.append(transaction)
            transaction_list = support_list
            break
        elif answer_for_currency == "нет":
            break
        else:
            print("Ответ не распознан")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        answer_for_description = input().lower()
        if answer_for_description == "да" or answer_for_description == "yes":
            print("Введите слово, по которому будем фильтровать список")
            user_description = input().lower()
            transaction_list = bank_operation(transaction_list, user_description)
            break
        elif answer_for_description == "нет":
            break
        else:
            print("Ответ не распознан")
    print("Распечатываю итоговый список транзакций...\n")
    if len(transaction_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transaction_list)}")
        if user_answer == "1":
            for transaction in transaction_list:
                if transaction["description"] == "Открытие вклада":
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["to"])}\nСумма: {transaction["operationAmount"]["amount"]} "
                          f"{transaction["operationAmount"]["currency"]["name"]}")
                else:
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}\n"
                          f"Сумма: {transaction["operationAmount"]["amount"]} "
                          f"{transaction["operationAmount"]["currency"]["name"]}")
        else:
            for transaction in transaction_list:
                if transaction["currency_name"] == 'Ruble':
                    transaction["currency_name"] = "руб."
                if transaction["description"] == "Открытие вклада":
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["to"])}\nСумма: {transaction["amount"]} "
                          f"{transaction["currency_name"]}")
                else:
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}\n"
                          f"Сумма: {transaction["amount"]} {transaction["currency_name"]}")


if __name__ == "__main__":
    main()
