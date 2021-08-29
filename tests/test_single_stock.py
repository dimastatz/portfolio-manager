import unittest
import pandas as pd
from src.single_stock import *


class TestSingleStock(unittest.TestCase):
    def test_quater_calc(self):
        symbol = ('MSFT', '2012-01-01', '2012-12-31')
        df = read_stock_dataframe(symbol[1], symbol[2], symbol[0])
        quaters = df['Quater'].unique()
        all_quaters = set(['1Q2012', '2Q2012', '3Q2012', '4Q2012'])
        self.assertEqual(len(set(quaters).difference(all_quaters)), 0)


    def test_load_stock_data(self):
        symbol = ('MSFT', '2012-01-01', '2012-01-31')
        df = read_stock_dataframe(symbol[1], symbol[2], symbol[0])
        self.assertEqual(20, df.shape[0])
        
        df = get_rolling_x_day_return(df, 'Adj Close', 10)
        rolling_return = df.at[pd.to_datetime('2012-01-17'), 'Rolling Return']
        self.assertEqual(5.57, rolling_return)
       
        holding_return = get_holding_period_return(df, '2012-01-03', '2012-01-09', 'Adj Close')
        self.assertEqual(3.62, holding_return)

        df = get_market_timing(df, 'Rolling Return')

    
    def test_quater_result(self):
        df = read_quater_res('MSFT')
        print('\nRES\n', df.columns)