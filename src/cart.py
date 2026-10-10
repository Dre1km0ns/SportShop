"""Корзина покупателя. Позиция: {'product_id', 'name', 'size', 'quantity', 'price'}."""
from src.catalog import find_product


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
    # hotfix: цена и количество могут прийти строками (из JSON/ввода) — приводим к числам
    return round(sum(float(i['price']) * int(i['quantity']) for i in cart), 2)


def total_sum(cart):
    """Синоним cart_total (имя из практического занятия №8)."""
    return cart_total(cart)
