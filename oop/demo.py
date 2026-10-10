"""Демонстрация объектной модели: python -m oop.demo"""
from oop.models import Apparel, Cart, Catalog, Footwear, Product, Shop

catalog = Catalog([
    Footwear(1, "Air Zoom Pegasus 40", "Nike", 11990, {40: 4, 41: 3}, gender="мужская"),
    Footwear(2, "Ultraboost Light", "Adidas", 15490, {41: 1, 42: 1}),
    Apparel(3, "Футболка Dri-FIT", "Nike", 2990, {"M": 8, "L": 4}, material="полиэстер"),
    Product(4, "Мяч футбольный", "Adidas", "Инвентарь", 3490, {5: 10}),
])
print("Товаров в каталоге:", len(catalog))
for p in catalog.search("nike"):
    print(" ", p.describe())
print("Низкий остаток:", [p.name for p in catalog.low_stock()])
print("По категориям:", catalog.count_by_category())

shop, cart = Shop(catalog), Cart()
print(cart.add(catalog.find(1), 40, 2))
print(cart.add(catalog.find(3), "M", 1))
print(cart.add(catalog.find(2), 39, 1))
print("Сумма корзины:", cart.total())
order = shop.checkout(cart, "[Клиент]")
print(order.receipt())
print("Остаток Pegasus р.40:", catalog.find(1).stock(40))
print("Выручка:", shop.revenue(), "| Лидер продаж:", shop.best_seller())
