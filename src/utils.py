import json
import logging
from json import JSONDecodeError

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(filename)s: %(funcName)s (строка вызова %(lineno)s): %(asctime)s - %(message)s",
    filename="../logs/utils.log",
    encoding="utf-8",
    filemode="w",
)

get_operations_data_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()


def get_transactions_dictionary(path: str = None) -> list:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logging.info(f'Получаем данные из файла {path}')
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions = json.load(operations)
            except JSONDecodeError:
                logging.error(f'Ошибка чтения JSON-файла {path}')
                return []
        if not isinstance(transactions, list):
            logging.critical('Список транзакций пуст')
            return []
        return transactions
    except FileNotFoundError as ex:
        logging.error(f'Данные не найдены: {ex}')
        return []


transaction = get_transactions_dictionary("../data/operations.json")
print(transaction)
