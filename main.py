"""СпортТовары — консольное приложение управления магазином.

Запуск: python main.py          — интерактивное меню
        python main.py --demo   — демонстрационный сценарий без ввода (используется build.py)
"""
import sys

from src.catalog import get_low_stock, search_advanced, count_by_category, avg_price, total_quantity
from src.cart import add_to_cart, remove_from_cart, update_quantity, cart_total
from src.orders import create_order, print_order, save_orders, load_orders
from src.analytics import total_revenue, best_selling_product, average_order_total
from src.storage import load_products, save_products

PRODUCTS_FILE = 'data/products.json'
ORDERS_FILE = 'data/orders.json'

MENU = """
===== СпортТовары =====
1. Каталог
2. Поиск товара
3. Товары с низким остатком
4. Добавить в корзину
5. Показать корзину
6. Изменить количество / удалить из корзины
7. Оформить заказ
8. Аналитика
9. Список заказов
0. Выход"""


def show_catalog(products):
    print(f"{'ID':<3} {'Название':<26} {'Бренд':<8} {'Категория':<10} {'Цена':>9}  Размеры (остаток)")
    for p in products:
        sizes = ', '.join(f'{s}:{q}' for s, q in p['sizes'].items())
        print(f"{p['id']:<3} {p['name']:<26} {p['brand']:<8} {p['category']:<10} {p['price']:>9.2f}  {sizes}")


def show_cart(cart):
    if not cart:
        print('Корзина пуста')
        return
    for i in cart:
        print(f"  [{i['product_id']}] {i['name']} р.{i['size']} x{i['quantity']} = {i['price'] * i['quantity']:.2f}")
    print(f'Итого: {cart_total(cart):.2f} руб.')


def show_analytics(products, orders):
    print('Товаров по категориям:', count_by_category(products))
    print(f'Средняя цена товара: {avg_price(products):.2f} руб.')
    print(f'Заказов: {len(orders)}, выручка: {total_revenue(orders):.2f} руб., '
          f'средний чек: {average_order_total(orders):.2f} руб.')
    print('Самый продаваемый товар:', best_selling_product(orders) or 'нет продаж')


def show_low_stock(products):
    low = get_low_stock(products)
    if not low:
        print('Нет товаров с низким остатком')
    for p in low:
        print(f"  {p['name']} — осталось {total_quantity(p)} шт.")


def parse_size(text):
    text = text.strip()
    return int(text) if text.isdigit() else text


def ask_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return -1


def interactive():
    products = load_products(PRODUCTS_FILE)
    orders = load_orders(ORDERS_FILE)
    cart = []
    while True:
        print(MENU)
        choice = input('Выберите пункт: ').strip()
        if choice == '1':
            show_catalog(products)
        elif choice == '2':
            query = input('Название или бренд: ')
            category = input('Категория (Enter — любая): ').strip() or None
            found = search_advanced(products, query, category)
            show_catalog(found) if found else print('Ничего не найдено')
        elif choice == '3':
            show_low_stock(products)
        elif choice == '4':
            pid = ask_int('ID товара: ')
            size = parse_size(input('Размер: '))
            print(add_to_cart(cart, products, pid, size, ask_int('Количество: '))[1])
        elif choice == '5':
            show_cart(cart)
        elif choice == '6':
            pid = ask_int('ID товара: ')
            size = parse_size(input('Размер: '))
            qty = ask_int('Новое количество (0 — удалить): ')
            print(update_quantity(cart, products, pid, size, qty)[1] if qty >= 0 else 'Неверное количество')
        elif choice == '7':
            order = create_order(cart, input('Имя клиента: '), products)
            if order:
                orders.append(order)
                save_orders(orders, ORDERS_FILE)
                save_products(products, PRODUCTS_FILE)
                print_order(order)
            else:
                print('Не удалось оформить заказ (корзина пуста, нет имени или нет остатка)')
        elif choice == '8':
            show_analytics(products, orders)
        elif choice == '9':
            for o in orders:
                print(f"  №{o['id']} {o['date']} {o['client']}: {o['total']:.2f} руб.")
            if not orders:
                print('Заказов нет')
        elif choice == '0':
            print('До свидания!')
            break
        else:
            print('Неизвестный пункт меню')


def demo():
    """Неинтерактивный сценарий: каталог → поиск → корзина → заказ → JSON → аналитика."""
    products = load_products(PRODUCTS_FILE)  # исходный файл не изменяется в демо
    print('--- Каталог ---')
    show_catalog(products)
    print('\n--- Поиск "nike" ---')
    show_catalog(search_advanced(products, 'nike'))
    print('\n--- Низкий остаток ---')
    show_low_stock(products)
    cart = []
    print('\n--- Корзина ---')
    print(add_to_cart(cart, products, 1, 40, 2)[1])
    print(add_to_cart(cart, products, 4, 'M', 1)[1])
    print(add_to_cart(cart, products, 2, 99, 1)[1])
    show_cart(cart)
    print('\n--- Заказ ---')
    order = create_order(cart, 'Демо-клиент', products)
    print_order(order)
    demo_file = 'data/demo_orders.json'
    save_orders([order], demo_file)
    loaded = load_orders(demo_file)
    print(f'Сохранено и загружено заказов: {len(loaded)}')
    import os
    os.remove(demo_file)
    print('\n--- Аналитика ---')
    show_analytics(products, loaded)


if __name__ == '__main__':
    demo() if '--demo' in sys.argv else interactive()
