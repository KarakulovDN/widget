# Виджет банковских операций
## Описание проекта

Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.

## Project dependencies:
* Python 3.12.4
* flake8 = "7.1.1"
* black = "24.10.0"
* isort = "5.13.2"
* mypy = "1.13.0"

## Функции, которые мы будем использовать:
* Функция скрывающая номер карты и счета
* Функция сортировки по дате
* Функция фильтрации в операциях по счетам
* Тестирование проекта с помощью pytest
* Функция вывода типа совершенной операции
* Функция фильтрации словаря по валюте
* Функция генерации номера карты

## Структура проекта:
* __tests__\ - папка содержит тесты проекта.
* ----- conftest.py
* ----- test_generators.py
* ----- test_masks.py
* ----- test_processing.py
* ----- test_widget.py


* __src__\ - папка содержит файлы с функциями проекта.
* ----- generators.py
* ----- masks.py
* ----- processing.py
* ----- widget.py 

## Покрытие pytest:
tests\test_generators.py ...                  [ 27%] 

tests\test_masks.py ..                        [ 45%] 

tests\test_processing.py ....                 [ 81%]

tests\test_widget.py ..                       [100%]


#### Name                       Stmts   Miss  Cover

----------------------------------------------       
src\__init__.py                0      0   100%       
src\generators.py             16      1    94%       
src\masks.py                  26      0   100%       
src\processing.py              6      0   100%       
src\widget.py                 31      1    97%       
tests\__init__.py              0      0   100%       
tests\conftest.py             71      0   100%       
tests\test_generators.py      22      0   100%       
tests\test_masks.py           12      0   100%       
tests\test_processing.py      15      0   100%       
tests\test_widget.py          20      0   100%       
----------------------------------------------       
TOTAL                        219      2    99%       

================ 11 passed in 0.11s ================ 


## Инструкция по установке
1. `git clone https://github.com/KarakulovDN/widget.git`
2. `pip install -r requirements.txt`
