# Виджет банковских операций
## Описание проекта

Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.

## Project dependencies:
* Python 3.12.4
* flake8 = "7.1.1"
* black = "24.10.0"
* isort = "5.13.2"
* mypy = "1.13.0"
* arrow = "^1.3.0"
* pytest = "^8.3.3"
* python-dotenv = "^1.0.1"
* requests = "^2.32.3"
* load-dotenv = "^0.1.0"
* logging = "^0.4.9.6"
* pandas = "^2.2.3"

## Функции, которые мы будем использовать:
* Функция скрывающая номер карты и счета
* Функция сортировки по дате
* Функция фильтрации в операциях по счетам
* Тестирование проекта с помощью pytest
* Функция вывода типа совершенной операции
* Функция фильтрации словаря по валюте
* Функция генерации номера карты
* Функция чтения файлов формата csv и excel

## Структура проекта:
* __tests__\ - папка содержит тесты проекта.
* ----- conftest.py
* ----- test_generators.py
* ----- test_masks.py
* ----- test_processing.py
* ----- test_widget.py
* ----- test_decorators.py
* ----- test_external_api.py
* ----- test_utils.py
* ----- test_data_file.py


* __src__\ - папка содержит файлы с функциями проекта.
* ----- generators.py
* ----- masks.py
* ----- processing.py
* ----- widget.py 
* ----- decorators.py
* ----- external_api.py
* ----- utils.py
* ----- data_file.py

* __logs__\ - папка содержит логи функций.

## Покрытие pytest:
tests\test_decorators.py .....                [ 31%] 

tests\test_generators.py ...                  [ 50%] 

tests\test_masks.py ..                        [ 62%]

tests\test_processing.py ....                 [ 87%]

tests\test_widget.py ..                       [100%]

#### Name                       Stmts   Miss  Cover

----------------------------------------------       
src\__init__.py                  0      0   100%     
src\decorators.py               17      0   100%     
src\external_api.py             14      1    93%     
src\generators.py               16      1    94%     
src\masks.py                    26      0   100%     
src\processing.py                6      0   100%     
src\utils.py                    24      5    79%     
src\widget.py                   31      1    97%     
tests\__init__.py                0      0   100%     
tests\conftest.py               71      0   100%     
tests\test_decorators.py        31      0   100%     
tests\test_external_api.py      10      0   100%     
tests\test_generators.py        22      0   100%     
tests\test_masks.py             12      0   100%     
tests\test_processing.py        15      0   100%     
tests\test_utils.py             23      0   100%     
tests\test_widget.py            20      0   100%     
------------------------------------------------     
TOTAL                          338      8    98%
================ 16 passed in 0.12s ================ 


## Инструкция по установке
1. `git clone https://github.com/KarakulovDN/widget.git`
2. `pip install -r requirements.txt`
