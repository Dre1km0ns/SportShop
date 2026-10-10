"""Практическая работа №4. Объектно-ориентированная модель ИС «СпортТовары»."""
from datetime import datetime


class Product:
    """Товар: название, бренд, категория, цена и остатки по размерам."""
    LOW_STOCK_LIMIT = 3

    def __init__(self, id, name, brand, category, price, sizes):
        self.id = id
        self.name = name
        self.brand = brand
        self.category = category
        self.price = float(price)
        self._sizes = dict(sizes)  # инкапсуляция: меняется только через методы

    def total_quantity(self):
        return sum(self._sizes.values())

    def is_low_stock(self):
        return self.total_quantity() <= self.LOW_STOCK_LIMIT

    def has_size(self, size):
        return size in self._sizes

    def stock(self, size):
        return self._sizes.get(size, 0)

    def write_off(self, size, qty):
        if self.stock(size) < qty:
            raise ValueError(f"Недостаточно товара {self.name} р.{size}")
        self._sizes[size] -= qty

    def describe(self):
        return f"{self.name} ({self.brand}) — {self.price:.2f} руб."

    def __repr__(self):
        return f"Product({self.id}, {self.name!r})"


class Footwear(Product):
    """Обувь — наследник Product с полом модели."""

    def __init__(self, id, name, brand, price, sizes, gender="унисекс"):
        super().__init__(id, name, brand, "Обувь", price, sizes)
        self.gender = gender

    def describe(self):
        return f"Обувь: {super().describe()}, {self.gender}"


class Apparel(Product):
    """Одежда — наследник Product с материалом."""

    def __init__(self, id, name, brand, price, sizes, material="полиэстер"):
        super().__init__(id, name, brand, "Одежда", price, sizes)
        self.material = material

    def describe(self):
        return f"Одежда: {super().describe()}, материал — {self.material}"


class Catalog:
    def __init__(self, products=None):
        self._products = list(products or [])

    def add(self, product):
        self._products.append(product)

    def find(self, product_id):
        return next((p for p in self._products if p.id == product_id), None)

    def search(self, query="", category=None, min_price=None, max_price=None):
        q = query.lower()
        return [p for p in self._products
                if q in f"{p.name} {p.brand}".lower()
                and (category is None or p.category == category)
                and (min_price is None or p.price >= min_price)
                and (max_price is None or p.price <= max_price)]

    def low_stock(self):
        return sorted((p for p in self._products if p.is_low_stock()), key=Product.total_quantity)

    def count_by_category(self):
        counts = {}
        for p in self._products:
            counts[p.category] = counts.get(p.category, 0) + 1
        return counts

    def __len__(self):
        return len(self._products)


class CartItem:
    def __init__(self, product, size, quantity):
        self.product = product
        self.size = size
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self._items = []

    def add(self, product, size, quantity):
        if not product.has_size(size):
            return False, f"Размер {size} отсутствует"
        item = next((i for i in self._items if i.product is product and i.size == size), None)
        already = item.quantity if item else 0
        if quantity <= 0 or already + quantity > product.stock(size):
            return False, "Недостаточно товара на складе"
        if item:
            item.quantity += quantity
        else:
            self._items.append(CartItem(product, size, quantity))
        return True, "Товар добавлен"

    def remove(self, product_id, size):
        before = len(self._items)
        self._items = [i for i in self._items if not (i.product.id == product_id and i.size == size)]
        return len(self._items) < before

    def total(self):
        return round(sum(i.subtotal() for i in self._items), 2)

    @property
    def items(self):
        return list(self._items)

    def clear(self):
        self._items.clear()


class Order:
    _counter = 0

    def __init__(self, client, items):
        Order._counter += 1
        self.id = Order._counter
        self.client = client
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.items = [(i.product.name, i.size, i.quantity, i.product.price) for i in items]
        self.total = round(sum(q * pr for _, _, q, pr in self.items), 2)

    def receipt(self):
        lines = [f"Заказ №{self.id} от {self.date}", f"Клиент: {self.client}"]
        lines += [f"  {n} р.{s} x{q} = {q * pr:.2f}" for n, s, q, pr in self.items]
        lines.append(f"Итого: {self.total:.2f} руб.")
        return "\n".join(lines)


class Shop:
    def __init__(self, catalog):
        self.catalog = catalog
        self.orders = []

    def checkout(self, cart, client):
        if not cart.items or not client.strip():
            return None
        for i in cart.items:
            i.product.write_off(i.size, i.quantity)
        order = Order(client, cart.items)
        self.orders.append(order)
        cart.clear()
        return order

    def revenue(self):
        return round(sum(o.total for o in self.orders), 2)

    def best_seller(self):
        sold = {}
        for o in self.orders:
            for name, _, qty, _ in o.items:
                sold[name] = sold.get(name, 0) + qty
        return max(sold, key=sold.get) if sold else None
