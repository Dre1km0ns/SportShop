import unittest

from src.catalog import get_low_stock, search_advanced, count_by_category, avg_price, find_product

P = [
    {'id': 1, 'name': 'Кроссовки X', 'brand': 'Nike', 'category': 'Обувь', 'price': 9000.0, 'sizes': {40: 1, 41: 1}},
    {'id': 2, 'name': 'Мяч', 'brand': 'Adidas', 'category': 'Инвентарь', 'price': 3000.0, 'sizes': {5: 20}},
]


class TestCatalog(unittest.TestCase):
    def test_low_stock(self):
        self.assertEqual([p['id'] for p in get_low_stock(P)], [1])

    def test_search_combined(self):
        self.assertEqual(search_advanced(P, 'мяч', 'Инвентарь', 1000, 5000)[0]['id'], 2)
        self.assertEqual(search_advanced(P, 'мяч', 'Обувь'), [])

    def test_count_by_category(self):
        self.assertEqual(count_by_category(P), {'Обувь': 1, 'Инвентарь': 1})

    def test_avg_price(self):
        self.assertEqual(avg_price(P), 6000.0)

    def test_find_product(self):
        self.assertEqual(find_product(P, 2)['name'], 'Мяч')
        self.assertIsNone(find_product(P, 3))

    def test_search_advanced_bad_range(self):
        with self.assertRaises(ValueError):
            search_advanced(P, '', min_price=100, max_price=10)


if __name__ == '__main__':
    unittest.main()
