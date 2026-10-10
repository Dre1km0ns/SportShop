"""Аналитика продаж."""


def total_revenue(orders):
    """Общая выручка по всем заказам."""
    return round(sum(o['total'] for o in orders), 2)


def best_selling_product(orders):
    """Название самого продаваемого товара (по количеству) или None."""
    sold = {}
    for o in orders:
        for i in o['items']:
            sold[i['name']] = sold.get(i['name'], 0) + i['quantity']
    if not sold:
        return None
    return max(sold, key=sold.get)


def average_order_total(orders):
    """Средняя сумма заказа (0 при отсутствии заказов)."""
    if not orders:
        return 0
    return round(total_revenue(orders) / len(orders), 2)
