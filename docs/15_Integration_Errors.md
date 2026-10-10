# Ошибки интеграции (занятие №9, задание 5)

## Какая ошибка была внесена?
В `src/cart.py` в функции `add_to_cart` при формировании позиции корзины ключ `'name'` был заменён на `'product'`:

```python
cart.append({'product_id': product_id, 'product': product['name'], 'size': size, ...})
```

Модули `orders.py` (`print_order`) и `analytics.py` (`best_selling_product`) по-прежнему ожидают ключ `'name'` —
типичная ошибка «несовместимость форматов данных в точке стыковки».

## Как она проявилась?
Модульные тесты самой функции `add_to_cart` на успех добавления продолжали проходить, но полный прогон упал:

```
ERROR: test_full_cycle (test_integration.TestIntegration.test_full_cycle)
KeyError: 'name'
ERROR: test_print_order (test_orders.TestOrders.test_print_order)
KeyError: 'name'
FAIL: test_item_format (test_cart.TestCart.test_item_format)
Ran 43 tests in 0.003s
FAILED (failures=1, errors=2)
```

## Как была исправлена?
По трассировке `KeyError: 'name'` в `analytics.best_selling_product` найдено место формирования позиции в `cart.py`;
ключ возвращён к `'name'`. Формат позиции корзины зафиксирован тестом `test_item_format`
(`{'product_id', 'name', 'size', 'quantity', 'price'}`) и описан в `docs/17_API_Reference.md`.
После исправления: `Ran 43 tests ... OK`.
