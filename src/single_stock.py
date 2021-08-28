import numpy as np
import pandas as pd
from pandas_datareader import data
from pandas.core.frame import DataFrame
from pandas.core.series import Series


# calculates return for the last x days in percents
def get_rolling_x_day_return(df: DataFrame, col: str, days: int) -> DataFrame:
    f = lambda x: round((x[-1:] - x[0]) * 100 / x[0], 2) 
    df['Rolling Return'] = df[col].rolling(days).apply(f)
    return df


# read stock data from yahoo finance 
# and return adjusted cose prices
def read_stock_dataframe(start: str, end: str, symbol: str) -> DataFrame:
    df = data.get_data_yahoo(symbol, start, end)
    return df[['Adj Close']]