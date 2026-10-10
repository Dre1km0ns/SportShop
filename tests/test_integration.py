"""Интеграционные тесты: полный цикл каталог → корзина → заказ → JSON."""
import os
import unittest

from src.catalog import get_low_stock
from src.cart import add_to_cart, cart_total
from src.orders import create_order, save_orders, load_orders
from src.storage import load_products
from src.analytics import total_revenue, best_selling_product

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.products = load_products(os.path.join(ROOT, 'data', 'products.json'))
        self.cart = []
        self.orders_file = os.path.join(ROOT, 'data', 'test_orders.json')

    def tearDown(self):
        if os.path.exists(self.orders_file):
            os.remove(self.orders_file)

    def test_full_cycle(self):
        result, msg = add_to_cart(self.cart, self.products, 1, 40, 2)
        self.assertTrue(result, msg)
        expected = cart_total(self.cart)
        order = create_order(self.cart, 'Тестовый клиент', self.products)
        self.assertIsNotNone(order)
        self.assertGreater(order['total'], 0)
        save_orders([order], self.orders_file)
        loaded = load_orders(self.orders_file)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]['total'], order['total'])
        self.assertEqual(loaded[0]['total'], expected)
        self.assertEqual(total_revenue(loaded), expected)
        self.assertEqual(best_selling_product(loaded), self.products[0]['name'])

    def test_sizes_loaded_as_numbers(self):
        self.assertIn(40, self.products[0]['sizes'])

    def test_low_stock_after_order(self):
        add_to_cart(self.cart, self.products, 1, 40, 4)
        add_to_cart(self.cart, self.products, 1, 41, 3)
        create_order(self.cart, 'Клиент', self.products)
        self.assertIn(1, [p['id'] for p in get_low_stock(self.products)])


if __name__ == '__main__':
    unittest.main()
