"""Заказы: создание, вывод, сохранение и загрузка JSON."""
import json
import os
from datetime import datetime

from src.cart import cart_total
from src.catalog import find_product


def create_order(cart, client_name, products):
    """Создаёт заказ из корзины и списывает остатки. Возвращает заказ или None."""
    if not cart or not client_name.strip():
        return None
    for item in cart:
        product = find_product(products, item['product_id'])
        if product is None or product['sizes'].get(item['size'], 0) < item['quantity']:
            return None
    for item in cart:
        find_product(products, item['product_id'])['sizes'][item['size']] -= item['quantity']
    order = {
        'id': datetime.now().strftime('%Y%m%d%H%M%S%f'),
        'client': client_name.strip(),
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'items': [dict(i) for i in cart],
        'total': cart_total(cart),
    }
    cart.clear()
    return order


def print_order(order):
    """Печатает заказ и возвращает текст."""
    lines = [f"Заказ №{order['id']} от {order['date']}", f"Клиент: {order['client']}"]
    for i in order['items']:
        lines.append(f"  {i['name']} (р. {i['size']}) x{i['quantity']} = {i['price'] * i['quantity']:.2f} руб.")
    lines.append(f"Итого: {order['total']:.2f} руб.")
    text = '\n'.join(lines)
    print(text)
    return text


def save_orders(orders, filename='data/orders.json'):
    """Сохраняет список заказов в JSON."""
    folder = os.path.dirname(filename)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)


def load_orders(filename='data/orders.json'):
    """Загружает заказы из JSON (пустой список, если файла нет)."""
    if not os.path.exists(filename):
        return []
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
