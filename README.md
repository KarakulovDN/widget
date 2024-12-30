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
* Функция чтения файлов формата json, csv и excel
* Функция поиска в списке словаре операций по описанию
* Функция для подсчета количества банковских операций определенного типа

## Структура проекта:
* main.py  — это пользовательский интерфейс программы, который объединяет весь функционал.


* __src__\ — папка содержит файлы с функциями проекта.
* ----- generators.py
* ----- masks.py
* ----- processing.py
* ----- widget.py 
* ----- decorators.py
* ----- external_api.py
* ----- utils.py
* ----- data_file.py
* ----- operation_name.py


* __tests__\ — папка содержит тесты проекта.
* ----- conftest.py
* ----- test_generators.py
* ----- test_masks.py
* ----- test_processing.py
* ----- test_widget.py
* ----- test_decorators.py
* ----- test_external_api.py
* ----- test_utils.py
* ----- test_data_file.py
* ----- test_operation_name.py


* __logs__\ — папка содержит логи функций.

## Покрытие pytest:
tests\test_data_file.py ....                               [ 13%]   
tests\test_decorators.py .....                             [ 31%]   
tests\test_external_api.py ...                             [ 41%]   
tests\test_generators.py ...                               [ 51%]   
tests\test_masks.py ..                                     [ 58%]   
tests\test_operation_name.py ...                           [ 68%]
tests\test_processing.py ....                              [ 82%]   
tests\test_utils.py ...                                    [ 93%]   
tests\test_widget.py ..                                    [100%]


#### Name   Stmts    Miss    Cover

----------------------------------------------       
src\__init__.py                    0      0   100%  
src\data_file.py                  21      5    76%  
src\decorators.py                 17      0   100%  
src\external_api.py               19      1    95%  
src\generators.py                 16      1    94%  
src\masks.py                      42      0   100%  
src\operation_name.py             23      5    78%  
src\processing.py                  7      0   100%  
src\utils.py                      27      5    81%  
src\widget.py                     32      2    94%  
tests\__init__.py                  0      0   100%  
tests\conftest.py                 74      0   100%  
tests\test_data_file.py           19      0   100%  
tests\test_decorators.py          31      0   100%  
tests\test_external_api.py        21      0   100%  
tests\test_generators.py          22      0   100%  
tests\test_masks.py               12      0   100%  
tests\test_operation_name.py       7      0   100%  
tests\test_processing.py          15      0   100%  
tests\test_utils.py               22      1    95%  
tests\test_widget.py              20      0   100%  

--------------------------------------------------
TOTAL                            447     20    96%


====================== 29 passed in 1.36s ======================= 


## Инструкция по установке
1. `git clone https://github.com/KarakulovDN/widget.git`
2. `pip install -r requirements.txt`
