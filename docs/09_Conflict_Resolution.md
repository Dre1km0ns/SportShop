# Разрешение конфликта в total_sum

## Как возник конфликт
1. От `develop` созданы ветки `feature/total-v1` и `feature/total-v2`.
2. В обеих ветках в конец `shop.py` добавлена функция `total_sum` — в одном и том же месте файла:
   - v1: `return sum(p['price'] for p in products)` — сумма цен без учёта количества;
   - v2: `return sum(p['price'] * p['quantity'] for p in products)` — с учётом количества.
3. `git merge feature/total-v1` выполнился перемоткой (fast-forward).
4. `git merge feature/total-v2` завершился сообщением
   `CONFLICT (content): Merge conflict in shop.py`, `git status` показал `UU shop.py`.

## Маркеры конфликта
```
<<<<<<< HEAD
def total_sum(products):
    return sum(p['price'] for p in products)
=======
def total_sum(products):
    return sum(p['price'] * p['quantity'] for p in products)
>>>>>>> feature/total-v2
```

## Решение
Оставлена правильная версия — **с учётом количества** (v2): сумма корзины = Σ цена × количество.
Маркеры `<<<<<<<`, `=======`, `>>>>>>>` удалены, тесты пройдены, затем:
```
git add shop.py
git commit -m "Разрешён конфликт в total_sum"
```

## Как избегать конфликтов
Короткие ветки, частое слияние `develop` в рабочую ветку, договорённость, кто какие функции меняет.
