# Функции по фильтрации данных из словарей

## Описание:
Этот проект включает функции для фильтрации и сортировки транзакций по состоянию и дате.

## Установка:
1. Клонируйте репозиторий:
```
git clone git@github.com:erkinov180903/homework_10_1.git
```

## Примеры использования

### Фильтрация транзакций по состоянию EXECUTED или CANCELLED

```python
from processing import filter_by_state

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2021-01-01'},
    {'id': 2, 'state': 'CANCELLED', 'date': '2021-02-01'}
]

filtered = filter_by_state(transactions, state="EXECUTED")
print(filtered)  # выведет [{'id': 1, 'state': 'EXECUTED', 'date': '2021-01-01'}]

### Фильтрация транзакций по дате

from processing import sort_by_date

transactions = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

sorted_transactions = sort_by_date(transactions, ascending=True)
print(sorted_transactions) # выведет список по возрастанию даты
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

## Лицензия
Этот проект лицензируется в соответствии с MIT License.
