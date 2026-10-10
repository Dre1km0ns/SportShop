# Hotfix: cart_total возвращает неверную сумму / падает

**Ветка:** `hotfix/cart-total` (от `main`) → `main` (тег `v1.0.1`) и `develop`.

## Ошибка
Если цена или количество позиции приходят строками (например, после загрузки заказа из JSON,
отредактированного вручную, или из неочищенного ввода), `cart_total` давала
`TypeError: can't multiply sequence by non-int of type 'str'` вместо суммы.

## Исправление
В `cart_total` значения приводятся к числам: `float(i['price']) * int(i['quantity'])`.
Добавлен регрессионный тест `TestCartTotalHotfix.test_string_values`.

## Порядок действий
```
git checkout main
git checkout -b hotfix/cart-total
# исправление + тест, git commit
git checkout main && git merge hotfix/cart-total && git tag -a v1.0.1
git checkout develop && git merge hotfix/cart-total
git branch -d hotfix/cart-total
```
