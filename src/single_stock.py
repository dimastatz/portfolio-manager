import numpy as np
import pandas as pd
from scipy import stats
from pandas_datareader import data


# holding period return -  
def get_holding_period_return(start_price: float, end_price: float) -> float:
    return (end_price - start_price) / start_price


# calculates return for the last x days
def get_xday_return(price_list: list, days: int, current_idx: int) -> float:
    return get_holding_period_return(price_list[current_idx - days], price_list[current_idx])


# computing time series momentum
def get_market_timing(returns_lst: list, current: float) -> float:
    return stats.percentileofscore(returns_lst, current)


# read stock data from yahoo finance
def read_stock_dataframe(start: str, end: str, symbol: str) -> pd.core.frame.DataFrame:
    return data.get_data_yahoo(symbol, start, end) 

