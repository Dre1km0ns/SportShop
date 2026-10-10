# СпортТовары — система управления магазином

## Описание
Консольное приложение для магазина спортивных товаров: каталог с размерами и остатками, поиск,
контроль низких остатков, корзина, оформление заказов с сохранением в JSON и аналитика продаж.
Проект выполнен в рамках практических работ №1–10 учебной практики.

## Практические работы
| № | Тема | Где в репозитории | Тег |
|---|---|---|---|
| 1–3 | Анализ, ТЗ, архитектура | `analysis/` | practice-1…3 |
| 4 | ООП-проектирование | `oop/`, `tests/test_oop.py` | practice-4 |
| 5 | Основы Python | `examples/pr5_basics.py` | practice-5 |
| 6 | Scrum/Kanban | `docs/03–07` | practice-6 |
| 7 | Git Flow, конфликты, PR, hotfix | `docs/08–12`, ветки develop/feature/hotfix | practice-7, v1.0.1 |
| 8 | unittest, отладка | `tests/`, `docs/13–14` | practice-8 |
| 9 | Интеграция, сборка | `src/`, `build.py`, `docs/15–16` | practice-9 |
| 10 | Документация, релиз | `docs/17–21` | practice-10, v1.0 |

Учебная ОС StudyOS (занятия 1–2): https://github.com/Dre1km0ns/my_os

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
├── analysis/       # ПР №1–3: анализ, ТЗ, эскизный проект, диаграммы (DOT/PNG)
├── oop/            # ПР №4: объектная модель (models.py, demo.py)
├── examples/       # pr5_basics.py — практическая работа №5
├── main.py
├── build.py
├── shop.py         # фасад для совместимости с занятием №8
└── README.md
```

## Авторы
- [ФИО], группа [Группа]
