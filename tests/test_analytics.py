import unittest

from src.analytics import total_revenue, best_selling_product, average_order_total

ORDERS = [
    {'total': 300.0, 'items': [{'name': 'A', 'quantity': 3}]},
    {'total': 100.0, 'items': [{'name': 'B', 'quantity': 1}, {'name': 'A', 'quantity': 1}]},
]


class TestAnalytics(unittest.TestCase):
    def test_revenue(self):
        self.assertEqual(total_revenue(ORDERS), 400.0)

    def test_best_selling(self):
        self.assertEqual(best_selling_product(ORDERS), 'A')
        self.assertIsNone(best_selling_product([]))

    def test_average(self):
        self.assertEqual(average_order_total(ORDERS), 200.0)
        self.assertEqual(average_order_total([]), 0)


if __name__ == '__main__':
    unittest.main()
