import unittest
import single_stock as sc


class TestSingleStock(unittest.TestCase):
    def test_get_market_timing(self):
        res = sc.get_market_timing([4, 1, 2, 4], 3)
        self.assertTrue(res, 50)
