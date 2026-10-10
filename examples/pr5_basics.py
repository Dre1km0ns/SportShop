"""Практическая работа №5. Основы Python: структуры данных для предметной области
(в оригинале задания — «Чудо Обувь»; здесь — магазин «СпортТовары»)."""

print("Добро пожаловать в магазин «СпортТовары»!")

# Задание 2. Переменные, print, for, if
name = "Air Zoom Pegasus 40"
price = 11990.0
quantity = 5
in_stock = True
print("Товар:", name, "| Цена:", price, "руб. | В наличии:", in_stock)
for size in [40.0, 41.0, 42.0]:
    print("Размер:", size)
for i in range(3):
    print("Итерация", i)
if quantity <= 3:
    print("Мало на складе")
elif quantity <= 10:
    print("Достаточно на складе")
else:
    print("Много")

# Задание 3. Списки и словари
users = [
    {"login": "admin", "password": "admin", "role": "Администратор", "fio": "[ФИО администратора]"},
    {"login": "manager", "password": "manager", "role": "Менеджер", "fio": "[ФИО менеджера]"},
    {"login": "client", "password": "client", "role": "Клиент", "fio": "[ФИО клиента]"},
]
products = [
    {"name": "Air Zoom Pegasus 40", "brand": "Nike", "price": 11990.0, "sizes": {40: 4, 41: 3}},
    {"name": "Ultraboost Light", "brand": "Adidas", "price": 15490.0, "sizes": {41: 1, 42: 1}},
    {"name": "Gel-Kayano 30", "brand": "Asics", "price": 13990.0, "sizes": {39: 2, 40: 5}},
    # Задание 8.1: ещё два товара
    {"name": "Шорты беговые", "brand": "Puma", "price": 2490.0, "sizes": {48: 2, 50: 1}},
    {"name": "Футболка Dri-FIT", "brand": "Nike", "price": 2990.0, "sizes": {46: 6, 48: 8}},
]
for p in products:
    print(p["name"], "— всего:", sum(p["sizes"].values()), "шт.")


# Задание 4. Функции
def find_user(login):
    for u in users:
        if u["login"] == login:
            return u
    return None


def total_sum(cart):
    return sum(item["price"] * item["qty"] for item in cart)


print("Найден:", find_user("manager")["role"])

# Задание 5. Сортировка и фильтрация
for p in sorted(products, key=lambda p: p["price"]):
    print(f"{p['name']}: {p['price']}")
low = [p for p in products if sum(p["sizes"].values()) <= 3]
print("Мало на складе:", [p["name"] for p in low])

# Задание 6. Поиск по каталогу
query = "zoom"
print("Поиск:", [p["name"] for p in products if query in p["name"].lower()])
print("От 10000 до 14000:", [p["name"] for p in products if 10000 <= p["price"] <= 14000])

# Задание 7. Корзина
cart = [{"name": products[0]["name"], "price": products[0]["price"], "qty": 2},
        {"name": products[3]["name"], "price": products[3]["price"], "qty": 1}]
print("Сумма корзины:", total_sum(cart), "руб.")


# Задание 8. Самостоятельно
def get_sizes(product):
    return sorted(product["sizes"].keys())


def get_total_quantity(product):
    return sum(product["sizes"].values())


print("Размеры:", get_sizes(products[0]), "Всего:", get_total_quantity(products[0]))
print("По алфавиту:", [p["name"] for p in sorted(products, key=lambda p: p["name"])])
print("Дешевле 6000:", [p["name"] for p in products if p["price"] < 6000])
i = 0
while i < len(products):
    print(f"{i + 1}. {products[i]['name']}")
    i += 1

# Дополнительное задание: заказы
orders = [
    {"date": "2026-10-02", "client": "[Клиент 2]", "items": [{"name": "Ultraboost Light", "price": 15490.0, "qty": 1}]},
    {"date": "2026-10-01", "client": "[Клиент 1]", "items": cart},
]
for o in sorted(orders, key=lambda o: o["date"]):
    print(o["date"], o["client"], total_sum(o["items"]), "руб.")
