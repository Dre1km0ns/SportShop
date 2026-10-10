import unittest

from oop.models import Apparel, Cart, Catalog, Footwear, Product, Shop


def make():
    return Catalog([Footwear(1, "A", "Nike", 100, {40: 2}), Apparel(2, "B", "Puma", 50, {"M": 10}),
                    Product(3, "C", "X", "Инвентарь", 10, {5: 1})])


class TestOOP(unittest.TestCase):
    def test_inheritance(self):
        c = make()
        self.assertIsInstance(c.find(1), Product)
        self.assertIn("Обувь", c.find(1).describe())
        self.assertIn("материал", c.find(2).describe())

    def test_search_and_low_stock(self):
        c = make()
        self.assertEqual([p.id for p in c.search("nike")], [1])
        self.assertEqual([p.id for p in c.low_stock()], [3, 1])
        self.assertEqual(c.count_by_category(), {"Обувь": 1, "Одежда": 1, "Инвентарь": 1})

    def test_cart(self):
        c, cart = make(), Cart()
        self.assertTrue(cart.add(c.find(1), 40, 2)[0])
        self.assertFalse(cart.add(c.find(1), 40, 1)[0])
        self.assertFalse(cart.add(c.find(1), 99, 1)[0])
        self.assertEqual(cart.total(), 200)
        self.assertTrue(cart.remove(1, 40))

    def test_checkout(self):
        c, cart = make(), Cart()
        shop = Shop(c)
        cart.add(c.find(2), "M", 3)
        order = shop.checkout(cart, "Иван")
        self.assertEqual(order.total, 150)
        self.assertEqual(c.find(2).stock("M"), 7)
        self.assertEqual(shop.revenue(), 150)
        self.assertEqual(shop.best_seller(), "B")
        self.assertIsNone(shop.checkout(Cart(), "Иван"))

    def test_write_off_error(self):
        with self.assertRaises(ValueError):
            make().find(3).write_off(5, 2)


if __name__ == "__main__":
    unittest.main()
