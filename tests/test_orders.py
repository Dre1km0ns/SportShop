import io
import os
from contextlib import redirect_stdout
import tempfile
import unittest

from src.cart import add_to_cart
from src.orders import create_order, save_orders, load_orders, print_order


def products():
    return [{'id': 1, 'name': 'A', 'price': 100.0, 'sizes': {40: 3}}]


class TestOrders(unittest.TestCase):
    def test_create_order_decreases_stock(self):
        cart, p = [], products()
        add_to_cart(cart, p, 1, 40, 2)
        order = create_order(cart, 'Клиент', p)
        self.assertEqual(order['total'], 200.0)
        self.assertEqual(p[0]['sizes'][40], 1)
        self.assertEqual(cart, [])

    def test_empty_cart_or_name(self):
        self.assertIsNone(create_order([], 'Клиент', products()))
        cart, p = [], products()
        add_to_cart(cart, p, 1, 40, 1)
        self.assertIsNone(create_order(cart, '  ', p))

    def test_save_load(self):
        path = os.path.join(tempfile.mkdtemp(), 'o.json')
        save_orders([{'id': '1', 'total': 5, 'items': []}], path)
        self.assertEqual(load_orders(path)[0]['total'], 5)
        self.assertEqual(load_orders(path + '.missing'), [])

    def test_print_order(self):
        cart, p = [], products()
        add_to_cart(cart, p, 1, 40, 1)
        with redirect_stdout(io.StringIO()):
            text = print_order(create_order(cart, 'Иван', p))
        self.assertIn('Итого: 100.00', text)


if __name__ == '__main__':
    unittest.main()
