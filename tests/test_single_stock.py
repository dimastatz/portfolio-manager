import unittest
from src.single_stock import *


class TestSingleStock(unittest.TestCase):
    def test_get_market_timing(self):
        res = get_market_timing([4, 1, 2, 4], 3)
        self.assertTrue(res, 50)

    def test_load_stock_data(self):
        symbol = ('MSFT', '2012-01-01', '2012-01-11')
        df = read_stock_dataframe(symbol[1], symbol[2], symbol[0])
        self.assertEqual(7, df.shape[0])
        