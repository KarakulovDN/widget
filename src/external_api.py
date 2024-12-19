import os
from typing import Any

import requests
from dotenv import load_dotenv


def convert_from_i_to_rub(transaction: Any) -> Any:
    amount = float(transaction["amount"])   # получение суммы траты
    currency = transaction["currency"]  # получение валюты

    if currency == "RUB":
        return float(amount)

    elif currency != "RUB":
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return float(data["result"])

    else:
        raise ValueError(f"Неизвестная валюта {currency}.")
