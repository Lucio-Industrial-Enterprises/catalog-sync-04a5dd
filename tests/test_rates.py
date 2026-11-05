import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_express_rates(self):
        self.assertEqual(shipping_quote(2, "local", "express"), 15.0)
        self.assertEqual(shipping_quote(2, "regional", "express"), 18.0)

    def test_express_matches_standard_plus_surcharge(self):
        for zone in ("local", "regional"):
            self.assertAlmostEqual(
                shipping_quote(5, zone, "express"),
                shipping_quote(5, zone, "standard") + 7.0,
            )

    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", "overnight")
