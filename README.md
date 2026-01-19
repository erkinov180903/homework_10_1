# Проект для обработки банковских транзакций с функциями фильтрации и сортировки.

## Описание:
#Этот модуль предоставляет инструменты для работы с данными банковских операций:
Фильтрация транзакций по статусу выполнения
Сортировка транзакций по дате в разных направлениях

## Возможности:
Фильтрация операций по статусу выполнения (EXECUTED, CANCELED)

Сортировка операций по дате (от новых к старым или от старых к новым)

Простая интеграция в проекте

Полная типизация с аннотациями типов

Соответствие стандартам кода (PEP 8, flake8, mypy, isort)

## Установка:
1. Клонируйте репозиторий:
```
git clone git@github.com:erkinov180903/homework_10_1.git
```
##Принципы работы
#Фильтрация
Функция проходит по всем элементам списка
Проверяет значение ключа "state" в каждом словаре
Добавляет в результат только те элементы, где состояние совпадает с заданным
##Сортировка
## Примеры использования
Использует встроенную функцию sorted()
В качестве ключа сортировки использует значение ключа "date"
Направление сортировки контролируется параметром ascending

### Фильтрация транзакций по состоянию EXECUTED или CANCELLED
```python
from processing import filter_by_state
def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
 filtered_transactions = []
    for dictionary in transactions:
        if dictionary["state"] == state:
 filtered_transactions.append(dictionary)
    return filtered_transactions

transactions = [
 {'id': 1, 'state': 'EXECUTED', 'date': '2021-01-01'},
 {'id': 2, 'state': 'CANCELLED', 'date': '2021-02-01'}
]
"""пример 1"""
filtered = filter_by_state(transactions)
print(filtered) # выведет [{'id': 1, 'state': 'EXECUTED', 'date': '2021-01-01'}]
"""пример 2"""
filtered = filter_by_state(transactions, state="CANCELLED")
print(filtered) # выведет [{'id': 2, 'state': 'CANCELLED', 'date': '2021-02-01'}]
```
### Фильтрация транзакций по дате
```python
from processing import sort_by_date
def sort_by_date(transactions: List[Dict], ascending: bool = False) -> List[Dict]:
    return sorted(transactions, key=lambda x: x["date"], reverse=not ascending)
transactions = [
 {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
"""пример 1"""
sorted_transactions = sort_by_date(transactions, ascending=True)
print(sorted_transactions) # выведет список по возрастанию даты
[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
"""пример 2"""
sorted_transactions = sort_by_date(transactions)
print(sorted_transactions) # выведет список по убыванию даты
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
#Требования
Python 3.6+
Нет внешних зависимостей

#Поддержка и контакты
email:erkinov180903@gmail.com
tg.me:@tima_pro_0


## Лицензия
Этот проект лицензируется в соответствии с MIT License.
