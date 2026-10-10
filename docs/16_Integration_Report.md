# Отчёт об интеграции (занятие №9)

## Выделенные модули
| Модуль | Функции |
|---|---|
| `src/catalog.py` | get_low_stock, search_advanced, count_by_category, avg_price, find_product, total_quantity |
| `src/cart.py` | add_to_cart, remove_from_cart, update_quantity, cart_total, total_sum |
| `src/orders.py` | create_order, print_order, save_orders, load_orders |
| `src/analytics.py` | total_revenue, best_selling_product, average_order_total |
| `src/storage.py` | load_products, save_products |

Интеграция выполнялась **восходящим** способом: каталог → корзина → заказы → аналитика.
Файл `shop.py` оставлен как фасад, реэкспортирующий функции (для совместимости с `tests/test_shop.py`).

## Импорты
- `cart.py` → `from src.catalog import find_product`
- `orders.py` → `from src.cart import cart_total`, `from src.catalog import find_product`
- `main.py` → импортирует функции всех пяти модулей.
Циклических зависимостей нет: catalog ← cart ← orders; analytics и storage независимы.

## Интеграционные тесты (`tests/test_integration.py`)
- `test_full_cycle` — загрузка товаров → корзина → заказ → сохранение JSON → загрузка → сверка суммы и аналитики;
- `test_sizes_loaded_as_numbers` — согласованность формата размеров storage ↔ cart;
- `test_low_stock_after_order` — списание остатков заказом отражается в каталоге.

Всего тестов в проекте: 43 (модульные + интеграционные), все проходят.

## Найденные и исправленные ошибки
1. Ключи размеров из JSON — строки (исправлено в `storage.load_products`).
2. Умышленная ошибка `'product'` вместо `'name'` (см. `15_Integration_Errors.md`).
3. Интеграционный тест создавал файл заказов относительно текущего каталога — путь сделан абсолютным от корня проекта.

## Скрипт сборки `build.py`
1. `check_python_version()` — Python ≥ 3.10; 2. `install_dependencies()` — requirements.txt (отсутствует, зависимостей нет);
3. `check_data()` — наличие `data/products.json`; 4. `run_tests()` — `unittest discover`; 5. `run_app()` — `main.py --demo`.

Вывод `python build.py`:
```
[1/5] Python 3.13.5
[2/5] Внешних зависимостей нет (только стандартная библиотека)
[3/5] Проверка data/products.json
[4/5] Запуск тестов
Ran 43 tests in 0.002s

OK
[5/5] Запуск приложения (демо-сценарий)
--- Аналитика ---
Товаров по категориям: {'Обувь': 3, 'Одежда': 2, 'Инвентарь': 3}
Средняя цена товара: 7102.50 руб.
Заказов: 1, выручка: 26970.00 руб., средний чек: 26970.00 руб.
Самый продаваемый товар: Air Zoom Pegasus 40
Сборка успешна!
```
