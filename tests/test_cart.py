import unittest

from src.cart import add_to_cart, remove_from_cart, update_quantity, cart_total


def products():
    return [{'id': 1, 'name': 'A', 'price': 100.0, 'sizes': {40: 3, 41: 1}}]


class TestCart(unittest.TestCase):
    def test_add_and_total(self):
        cart, p = [], products()
        self.assertTrue(add_to_cart(cart, p, 1, 40, 2)[0])
        self.assertTrue(add_to_cart(cart, p, 1, 41, 1)[0])
        self.assertEqual(cart_total(cart), 300.0)

    def test_item_format(self):
        cart = []
        add_to_cart(cart, products(), 1, 40, 1)
        self.assertEqual(set(cart[0]), {'product_id', 'name', 'size', 'quantity', 'price'})

    def test_invalid_quantity(self):
        self.assertFalse(add_to_cart([], products(), 1, 40, 0)[0])

    def test_remove_and_update(self):
        cart, p = [], products()
        add_to_cart(cart, p, 1, 40, 1)
        self.assertTrue(update_quantity(cart, p, 1, 40, 3)[0])
        self.assertFalse(update_quantity(cart, p, 1, 40, -1)[0])
        self.assertTrue(remove_from_cart(cart, 1, 40))
        self.assertEqual(cart, [])


if __name__ == '__main__':
    unittest.main()
