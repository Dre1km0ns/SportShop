# Sprint Backlog — Спринт 1

**Длительность:** 1 неделя (одно занятие, 6 академических часов = 270 мин).
**Цель спринта:** базовые функции каталога, поиска, аналитики и сохранения заказов в `shop.py`.

### US-1. Товары с низким остатком (3 SP)
- [x] Написать функцию `get_low_stock(products)` — 30 мин
- [x] Сортировка по возрастанию остатка — 10 мин
- [x] Вывести список в консольном меню — 15 мин
- [x] Добавить тест `test_get_low_stock` — 15 мин

### US-2. Поиск товаров (5 SP)
- [x] Написать `search_advanced(products, query, category, min_price, max_price)` — 40 мин
- [x] Пункт меню «Поиск» — 15 мин

### US-3. Корзина (5 SP)
- [x] `add_to_cart` с проверкой размера и остатка — 30 мин
- [x] `cart_total` / `total_sum` — 10 мин

### US-4. Оформление заказа и JSON (8 SP)
- [x] `create_order` — 25 мин
- [x] `save_orders(orders, filename='orders.json')` / `load_orders` — 25 мин

### US-5. Аналитика по категориям (5 SP)
- [x] `count_by_category(products)` — 15 мин
- [x] `avg_price(products)` — 10 мин

**Суммарная трудоёмкость:** 240 мин (≈ 5,3 ак. ч) ≤ 6 ак. ч. Story points: 26.
