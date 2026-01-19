from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список транзакций по заданному состоянию."""
    filtered_transactions = []
    for dictionary in transactions:
        if dictionary["state"] == state:
            filtered_transactions.append(dictionary)
    return filtered_transactions


def sort_by_date(transactions: List[Dict], ascending: bool = False) -> List[Dict]:
    """Сортирует список транзакций по дате."""
    return sorted(transactions, key=lambda x: x["date"], reverse=not ascending)
