"""Совместимость со старыми занятиями: монолит shop.py разделён на модули src/ (занятие №9).

Модуль реэкспортирует функции, чтобы старый код и tests/test_shop.py продолжали работать.
"""
from src.catalog import get_low_stock, search_advanced, count_by_category, avg_price, find_product, total_quantity  # noqa: F401
from src.cart import add_to_cart, remove_from_cart, update_quantity, cart_total, total_sum  # noqa: F401
from src.orders import create_order, print_order, save_orders, load_orders  # noqa: F401
from src.analytics import total_revenue, best_selling_product, average_order_total  # noqa: F401
from src.storage import load_products, save_products  # noqa: F401
