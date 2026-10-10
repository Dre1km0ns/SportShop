# История коммитов (git log --oneline --graph --all)

```
*   7063c47 Release: develop -> main (практическое занятие 7)
|\  
| *   6260a87 Merge hotfix/cart-total into develop
| |\  
| * \   670712a Merge PR feature/search-advanced into develop
| |\ \  
| | * | 25e152d US-2: search_advanced — проверка диапазона цены, описание PR
| |/ /  
| * |   f531475 Разрешён конфликт в total_sum
| |\ \  
| | * | a9530de total_sum v2: сумма с учётом количества
| * | | 4ea40f9 total_sum v1: сумма цен
| |/ /  
| * | ddcf276 US-1: добавлена функция get_low_stock (отчёт low_stock_report в shop.py)
| * | 798816f docs: схема Git Flow (08_Git_Flow.md)
* | |   769c967 Merge hotfix/cart-total
|\ \ \  
| |/ /  
|/| /   
| |/    
| * a96c5d4 fix: cart_total приводит цену и количество к числам
|/  
* 7979e28 Practice 4: объектная модель (классы Product, Catalog, Cart, Order, Shop)
* 120da95 Practice 1-3: анализ предметной области, ТЗ, эскизный проект и диаграммы
* bd84017 Day 10: финальная документация и релиз v1.0
* 39c1a8c Day 9: интеграция модулей и сборка
* c9c3b34 Day 8: добавлены модульные тесты
* ea48c01 US-4: оформление заказа, save_orders/load_orders в JSON, аналитика
* e3fc205 US-3: корзина — add_to_cart, remove_from_cart, update_quantity, cart_total
* 9b471a5 US-1: добавлены get_low_stock, search_advanced (US-2), count_by_category и avg_price (US-5)
* 0e40644 Day 6: Product Backlog, Sprint Backlog, Kanban, стендап, ретроспектива
* 210b29a Day 5: основы Python, структуры данных каталога
```

## Анализ графа
**Сколько веток было создано?** В ходе занятия №7 создано 6 веток: `develop`, `feature/low-stock`,
`feature/total-v1`, `feature/total-v2`, `feature/search-advanced`, `hotfix/cart-total`. Постоянными остаются
`main` и `develop`; feature- и hotfix-ветки удалены после слияния (`feature/search-advanced` также опубликована
на GitHub по шагу 22).

**Какие слияния произошли?**
1. `feature/low-stock` → `develop` — перемотка (fast-forward), поэтому отдельного merge-коммита нет;
2. `feature/total-v1` → `develop` — перемотка;
3. `feature/total-v2` → `develop` — с конфликтом, merge-коммит «Разрешён конфликт в total_sum»;
4. `feature/search-advanced` → `develop` — merge-коммит (имитация Pull Request);
5. `hotfix/cart-total` → `main` (тег `v1.0.1`) и → `develop`;
6. `develop` → `main` — релиз занятия №7.

**Был ли конфликт и как он разрешён?** Да: обе ветки `feature/total-*` добавили `total_sum` в одно место
`shop.py`. Оставлена версия с учётом количества (`price * quantity`), маркеры удалены, выполнены
`git add shop.py` и `git commit -m "Разрешён конфликт в total_sum"` (подробно — `09_Conflict_Resolution.md`).
