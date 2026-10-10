"""Сохранение и загрузка каталога товаров в JSON."""
import json


def load_products(filename='data/products.json'):
    """Загружает товары. Ключи размеров приводятся к числам (в JSON они строки)."""
    with open(filename, encoding='utf-8') as f:
        products = json.load(f)
    for p in products:
        p['sizes'] = {_to_number(k): v for k, v in p['sizes'].items()}
    return products


def save_products(products, filename='data/products.json'):
    """Сохраняет товары в JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


def _to_number(key):
    try:
        number = float(key)
        return int(number) if number.is_integer() else number
    except (TypeError, ValueError):
        return key
