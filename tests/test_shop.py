"""Модульные тесты функций магазина (практическое занятие №8)."""
import unittest

from shop import get_low_stock, search_advanced, total_sum, cart_total
from shop import add_to_cart, remove_from_cart, update_quantity, count_by_category, avg_price

PRODUCTS = [
    {'id': 1, 'name': 'Air Zoom Pegasus', 'brand': 'Nike', 'category': 'Обувь', 'price': 10000.0, 'sizes': {40: 5, 41: 2}},
    {'id': 2, 'name': 'Ultraboost', 'brand': 'Adidas', 'category': 'Обувь', 'price': 15000.0, 'sizes': {42: 1}},
    {'id': 3, 'name': 'Мяч футбольный', 'brand': 'Adidas', 'category': 'Инвентарь', 'price': 3000.0, 'sizes': {5: 10}},
]


def fresh_products():
    return [dict(p, sizes=dict(p['sizes'])) for p in PRODUCTS]


class TestGetLowStock(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_low_stock([]), [])

    def test_no_low_stock(self):
        products = [{'name': 'A', 'sizes': {40: 10}}]
        self.assertEqual(get_low_stock(products), [])

    def test_one_low_stock(self):
        products = [
            {'name': 'A', 'sizes': {40: 1}},
            {'name': 'B', 'sizes': {40: 10}},
        ]
        result = get_low_stock(products)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'A')

    def test_boundary_three_and_sorted(self):
        products = [{'name': 'A', 'sizes': {40: 3}}, {'name': 'B', 'sizes': {40: 1}}, {'name': 'C', 'sizes': {40: 4}}]
        self.assertEqual([p['name'] for p in get_low_stock(products)], ['B', 'A'])


class TestSearchAdvanced(unittest.TestCase):
    def test_by_name(self):
        result = search_advanced(PRODUCTS, 'zoom')
        self.assertEqual([p['id'] for p in result], [1])

    def test_by_brand(self):
        self.assertEqual(len(search_advanced(PRODUCTS, 'adidas')), 2)

    def test_by_category(self):
        result = search_advanced(PRODUCTS, '', category='инвентарь')
        self.assertEqual([p['id'] for p in result], [3])

    def test_by_price(self):
        result = search_advanced(PRODUCTS, '', min_price=5000, max_price=12000)
        self.assertEqual([p['id'] for p in result], [1])

    def test_nothing_found(self):
        self.assertEqual(search_advanced(PRODUCTS, 'хоккей'), [])


class TestTotalSum(unittest.TestCase):
    def test_empty_cart(self):
        self.assertEqual(total_sum([]), 0)

    def test_cart_with_items(self):
        cart = [{'price': 100.0, 'quantity': 2}, {'price': 50.5, 'quantity': 1}]
        self.assertEqual(total_sum(cart), 250.5)
        self.assertEqual(cart_total(cart), 250.5)


class TestCatalogStats(unittest.TestCase):
    def test_count_by_category(self):
        self.assertEqual(count_by_category(PRODUCTS), {'Обувь': 2, 'Инвентарь': 1})

    def test_avg_price(self):
        self.assertEqual(avg_price(PRODUCTS), 9333.33)
        self.assertEqual(avg_price([]), 0)


class TestAddToCart(unittest.TestCase):
    def test_invalid_size(self):
        products = [{'id': 1, 'name': 'A', 'sizes': {40: 5}}]
        cart = []
        result, message = add_to_cart(cart, products, 1, 99, 1)
        self.assertFalse(result)
        self.assertIn('размер', message.lower())

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

    def test_success(self):
        cart = []
        ok, _ = add_to_cart(cart, fresh_products(), 1, 40, 2)
        self.assertTrue(ok)
        self.assertEqual(cart[0]['quantity'], 2)

    def test_repeat_increases_quantity(self):
        cart, products = [], fresh_products()
        add_to_cart(cart, products, 1, 40, 1)
        add_to_cart(cart, products, 1, 40, 2)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['quantity'], 3)

    def test_not_enough_stock(self):
        ok, msg = add_to_cart([], fresh_products(), 2, 42, 5)
        self.assertFalse(ok)
        self.assertIn('недостаточно', msg.lower())

    def test_unknown_product(self):
        self.assertFalse(add_to_cart([], fresh_products(), 99, 40, 1)[0])


class TestCartOperations(unittest.TestCase):
    def setUp(self):
        self.products = fresh_products()
        self.cart = []
        add_to_cart(self.cart, self.products, 1, 40, 1)
        add_to_cart(self.cart, self.products, 3, 5, 2)

    def test_remove(self):
        self.assertTrue(remove_from_cart(self.cart, 1, 40))
        self.assertEqual(len(self.cart), 1)
        self.assertFalse(remove_from_cart(self.cart, 1, 40))

    def test_update_quantity(self):
        ok, _ = update_quantity(self.cart, self.products, 3, 5, 4)
        self.assertTrue(ok)
        self.assertEqual(self.cart[1]['quantity'], 4)

    def test_update_quantity_zero_removes(self):
        update_quantity(self.cart, self.products, 1, 40, 0)
        self.assertEqual(len(self.cart), 1)

    def test_update_over_stock(self):
        self.assertFalse(update_quantity(self.cart, self.products, 1, 40, 100)[0])

    def test_cart_total(self):
        self.assertEqual(cart_total(self.cart), 16000.0)


if __name__ == '__main__':
    unittest.main()
