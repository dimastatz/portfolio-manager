import unittest
from src.single_stock import *


class TestSingleStock(unittest.TestCase):
    def test_load_stock_data(self):
        symbol = ('MSFT', '2012-01-01', '2012-01-31')
        df = read_stock_dataframe(symbol[1], symbol[2], symbol[0])
        self.assertEqual(20, df.shape[0])
        print(df)

        df = get_rolling_x_day_return(df, 'Adj Close', 10)
        print(df)
        