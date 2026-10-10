"""Работа с каталогом товаров."""

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
    if min_price is not None and max_price is not None and min_price > max_price:
        raise ValueError('min_price не может быть больше max_price')
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
