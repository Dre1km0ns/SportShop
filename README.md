# СпортТовары — система управления магазином

## Описание
Консольное приложение для магазина спортивных товаров: каталог с размерами и остатками, поиск,
контроль низких остатков, корзина, оформление заказов с сохранением в JSON и аналитика продаж.
Проект выполнен в рамках практических занятий №5, 6, 8, 9, 10.

## Требования
- Python 3.10+
- SQLite не используется: данные хранятся в JSON (`data/products.json`, `data/orders.json`).
- Внешних зависимостей нет.

## Установка
```bash
git clone <url-репозитория> SportShop
cd SportShop
```

## Использование
```bash
python main.py           # интерактивное меню
python main.py --demo    # демонстрационный сценарий без ввода
```
Пункты меню: каталог, поиск, низкий остаток, добавить в корзину, корзина, изменить количество,
оформить заказ, аналитика, список заказов. Подробно — [docs/18_User_Guide.md](docs/18_User_Guide.md).

## Тестирование
```bash
python -m unittest discover -s tests
```

## Сборка
```bash
python build.py
```

## Структура проекта
```
SportShop/
├── src/
│   ├── catalog.py
│   ├── cart.py
│   ├── orders.py
│   ├── analytics.py
│   └── storage.py
├── tests/          # test_shop, test_catalog, test_cart, test_orders, test_analytics, test_integration
├── docs/           # 03–07 Agile, 13–14 тесты, 15–16 интеграция, 17–21 документация
├── data/           # products.json
├── examples/       # pr5_basics.py — практическая работа №5
├── main.py
├── build.py
├── shop.py         # фасад для совместимости с занятием №8
└── README.md
```

## Авторы
- [ФИО], группа [Группа]
