# Справочник API — СпортТовары

Форматы данных:
- **товар** — `{'id': int, 'name': str, 'brand': str, 'category': str, 'price': float, 'sizes': {размер: остаток}}`;
- **позиция корзины** — `{'product_id': int, 'name': str, 'size': int|str, 'quantity': int, 'price': float}`;
- **заказ** — `{'id': str, 'client': str, 'date': 'YYYY-MM-DD HH:MM', 'items': [позиции], 'total': float}`.

---
## src/catalog.py

### `get_low_stock(products, limit=3)`
Возвращает товары с суммарным остатком ≤ `limit`, отсортированные по возрастанию остатка.
**Параметры:** `products` (list[dict]); `limit` (int, по умолчанию 3).
**Возвращает:** `list[dict]`.
**Пример:**
```python
for p in get_low_stock(products):
    print(p['name'])
```
**Исключения:** нет (отсутствующий ключ `sizes` считается пустым).

### `search_advanced(products, query, category=None, min_price=None, max_price=None)`
Комбинированный поиск: подстрока в названии или бренде (без учёта регистра), категория, диапазон цены.
**Параметры:** `query` (str, пустая строка — без фильтра); `category` (str|None); `min_price`, `max_price` (float|None).
**Возвращает:** `list[dict]`.
**Пример:** `search_advanced(products, 'nike', category='Обувь', max_price=12000)`
**Исключения:** `KeyError`, если у товара нет `price` при заданном фильтре цены.

### `count_by_category(products)`
**Назначение:** подсчёт позиций по категориям. **Возвращает:** `dict[str, int]`.
**Пример:** `count_by_category(products)  # {'Обувь': 3, 'Одежда': 2}` **Исключения:** нет.

### `avg_price(products)`
**Назначение:** средняя цена, округлённая до 2 знаков; 0 для пустого списка. **Возвращает:** `float`.
**Пример:** `avg_price(products)  # 7102.5` **Исключения:** `KeyError` при отсутствии `price`.

### `find_product(products, product_id)`
**Назначение:** поиск товара по id. **Возвращает:** `dict | None`. **Пример:** `find_product(products, 1)`. **Исключения:** нет.

### `total_quantity(product)`
**Назначение:** суммарный остаток по всем размерам. **Возвращает:** `int`. **Пример:** `total_quantity(p)  # 9`.

---
## src/cart.py

### `add_to_cart(cart, products, product_id, size, quantity)`
Добавляет товар; при повторном добавлении увеличивает количество. Проверяет наличие товара, размера, остатка.
**Параметры:** `cart` (list, изменяется на месте), `products` (list[dict]), `product_id` (int), `size` (int|str), `quantity` (int > 0).
**Возвращает:** `tuple[bool, str]` — успех и сообщение.
**Пример:**
```python
ok, msg = add_to_cart(cart, products, 1, 40, 2)
```
**Исключения:** не выбрасывает; ошибки возвращаются как `(False, 'Размер 99 отсутствует')`.

### `remove_from_cart(cart, product_id, size)`
**Назначение:** удаляет позицию. **Возвращает:** `bool` (была ли позиция). **Пример:** `remove_from_cart(cart, 1, 40)`.

### `update_quantity(cart, products, product_id, size, new_qty)`
**Назначение:** изменяет количество; `0` удаляет позицию. **Возвращает:** `tuple[bool, str]`.
**Пример:** `update_quantity(cart, products, 1, 40, 3)`. **Исключения:** нет (отрицательное количество → `(False, ...)`).

### `cart_total(cart)` / `total_sum(cart)`
**Назначение:** сумма корзины (`total_sum` — синоним из занятия №8). **Возвращает:** `float`.
**Пример:** `cart_total(cart)  # 26970.0`. **Исключения:** `KeyError` при неверном формате позиции.

---
## src/orders.py

### `create_order(cart, client_name, products)`
Создаёт заказ, списывает остатки, очищает корзину.
**Возвращает:** `dict` заказа или `None` (пустая корзина, пустое имя, нехватка остатка).
**Пример:** `order = create_order(cart, 'Иванов', products)`. **Исключения:** нет.

### `print_order(order)`
**Назначение:** печать заказа. **Возвращает:** `str` — напечатанный текст. **Пример:** `print_order(order)`.
**Исключения:** `KeyError` при неверном формате заказа.

### `save_orders(orders, filename='data/orders.json')`
**Назначение:** сохраняет заказы в JSON (UTF-8, с отступами), создаёт папку при необходимости. **Возвращает:** `None`.
**Пример:** `save_orders(orders)`. **Исключения:** `OSError` при отсутствии прав на запись.

### `load_orders(filename='data/orders.json')`
**Назначение:** загружает заказы. **Возвращает:** `list[dict]` (пустой, если файла нет).
**Пример:** `orders = load_orders()`. **Исключения:** `json.JSONDecodeError` при повреждённом файле.

---
## src/analytics.py

### `total_revenue(orders)`
**Назначение:** выручка. **Возвращает:** `float`. **Пример:** `total_revenue(orders)`. **Исключения:** `KeyError`.

### `best_selling_product(orders)`
**Назначение:** самый продаваемый товар по количеству единиц. **Возвращает:** `str | None`.
**Пример:** `best_selling_product(orders)  # 'Air Zoom Pegasus 40'`.

### `average_order_total(orders)`
**Назначение:** средний чек; 0 при отсутствии заказов. **Возвращает:** `float`. **Пример:** `average_order_total(orders)`.

---
## src/storage.py

### `load_products(filename='data/products.json')`
**Назначение:** загрузка каталога; ключи размеров приводятся к числам (`'40'` → `40`, `'M'` остаётся строкой).
**Возвращает:** `list[dict]`. **Пример:** `products = load_products()`.
**Исключения:** `FileNotFoundError`, `json.JSONDecodeError`.

### `save_products(products, filename='data/products.json')`
**Назначение:** сохранение каталога. **Возвращает:** `None`. **Пример:** `save_products(products)`. **Исключения:** `OSError`.
