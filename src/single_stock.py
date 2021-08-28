import pandas as pd
from pandas_datareader import data
from pandas.core.series import Series
from pandas.core.frame import DataFrame


# holding period return in percents
def get_holding_period_return(df: DataFrame, start, end, col) -> float:
    start_price = df.at[pd.to_datetime(start), col]
    end_price = df.at[pd.to_datetime(end), col]
    return round((end_price - start_price) * 100 / start_price, 2)


# calculates return for the last x days in percents
def get_rolling_x_day_return(df: DataFrame, col: str, days: int) -> DataFrame:
    def f(x: Series):
        return round((x[-1:] - x[0]) * 100 / x[0], 2)

    df['Rolling Return'] = df[col].rolling(days).apply(f)
    return df


def get_market_timing(df: DataFrame, col: str) -> DataFrame:
    df['{} Rank'.format(col)] = round(df[col].rank(pct=True) * 100, 2)
    return df


# read stock data from yahoo finance and return adjusted cose prices
def read_stock_dataframe(start: str, end: str, symbol: str) -> DataFrame:
    df = data.get_data_yahoo(symbol, start, end)
    return df[['Adj Close']]
