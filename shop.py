"""СпортТовары — монолитная версия (занятия 6–8). Функции каталога."""
import json
import os
from datetime import datetime


LOW_STOCK_LIMIT = 3


def total_quantity(product):
    """Суммарное количество единиц товара по всем размерам."""
    return sum(product.get('sizes', {}).values())


def get_low_stock(products, limit=LOW_STOCK_LIMIT):
    """Товары с суммарным остатком <= limit, по возрастанию остатка."""
    low = [p for p in products if total_quantity(p) <= limit]
    return sorted(low, key=total_quantity)


def search_advanced(products, query, category=None, min_price=None, max_price=None):
    """Комбинированный поиск: подстрока в названии/бренде + категория + диапазон цены."""
    query = (query or '').strip().lower()
    result = []
    for p in products:
        text = f"{p.get('name', '')} {p.get('brand', '')}".lower()
        if query and query not in text:
            continue
        if category and p.get('category', '').lower() != category.lower():
            continue
        if min_price is not None and p['price'] < min_price:
            continue
        if max_price is not None and p['price'] > max_price:
            continue
        result.append(p)
    return result


def count_by_category(products):
    """Словарь {категория: количество позиций}."""
    counts = {}
    for p in products:
        cat = p.get('category', 'Без категории')
        counts[cat] = counts.get(cat, 0) + 1
    return counts


def avg_price(products):
    """Средняя цена товаров (0 для пустого списка)."""
    if not products:
        return 0
    return round(sum(p['price'] for p in products) / len(products), 2)


def find_product(products, product_id):
    """Товар по id или None."""
    for p in products:
        if p['id'] == product_id:
            return p
    return None

# ---------- Корзина ----------


def add_to_cart(cart, products, product_id, size, quantity):
    """Добавляет товар в корзину. Возвращает (успех, сообщение)."""
    product = find_product(products, product_id)
    if product is None:
        return False, 'Товар не найден'
    if size not in product['sizes']:
        return False, f'Размер {size} отсутствует'
    if quantity <= 0:
        return False, 'Количество должно быть больше нуля'
    in_cart = sum(i['quantity'] for i in cart if i['product_id'] == product_id and i['size'] == size)
    if in_cart + quantity > product['sizes'][size]:
        return False, f'Недостаточно товара на складе (доступно {product["sizes"][size] - in_cart})'
    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            return True, 'Количество увеличено'
    cart.append({'product_id': product_id, 'name': product['name'], 'size': size,
                 'quantity': quantity, 'price': product['price']})
    return True, 'Товар добавлен в корзину'


def remove_from_cart(cart, product_id, size):
    """Удаляет позицию. Возвращает True, если позиция была найдена."""
    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            cart.remove(item)
            return True
    return False


def update_quantity(cart, products, product_id, size, new_qty):
    """Меняет количество позиции. new_qty == 0 удаляет позицию. Возвращает (успех, сообщение)."""
    if new_qty == 0:
        return (True, 'Позиция удалена') if remove_from_cart(cart, product_id, size) else (False, 'Позиция не найдена')
    if new_qty < 0:
        return False, 'Количество не может быть отрицательным'
    product = find_product(products, product_id)
    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            if product and new_qty > product['sizes'].get(size, 0):
                return False, 'Недостаточно товара на складе'
            item['quantity'] = new_qty
            return True, 'Количество изменено'
    return False, 'Позиция не найдена'


def cart_total(cart):
    """Сумма корзины."""
    return round(sum(i['price'] * i['quantity'] for i in cart), 2)


def total_sum(cart):
    """Синоним cart_total (имя из практического занятия №8)."""
    return cart_total(cart)
