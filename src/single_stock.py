import pandas as pd
from numpy import datetime64
from pandas_datareader import data
from pandas.core.series import Series
from pandas.core.frame import DataFrame
from yahoofinancials import YahooFinancials


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


# Rolling returns rank is based on the
# percentile stock's rolling returns fall into.
def get_market_timing(df: DataFrame, col: str) -> DataFrame:
    df['{} Rank'.format(col)] = round(df[col].rank(pct=True) * 100, 2)
    return df


def format_quater(dt: datetime64) -> str:
        return '{}Q{}'.format(int((dt.month - 1) / 3) + 1, dt.year)

# read stock data from yahoo finance and return adjusted cose prices
def read_stock_dataframe(start: str, end: str, symbol: str) -> DataFrame:
    df = data.get_data_yahoo(symbol, start, end)
    df['Quater'] = df.index
    df['Quater'] = df['Quater'].apply(format_quater)
    df = df[['Quater', 'Adj Close']]
    return df


# return df with the following columns
# Quarter, Shares Outstanding, Net Income, Total Sales, Book Value
def read_quater_res(symbol: str) -> DataFrame:
    df = {
        'Quater': [],
        'Book Value': [],
        'Net Income': [],
        'Total Sales': [],
        'Shares Outstanding': [],
    }
    stock = YahooFinancials(symbol)
    res = stock.get_financial_stmts('quarterly', 'income')
    for k in res['incomeStatementHistoryQuarterly'][symbol]:
        print(list(k.keys())[0])
        #print('HERE:\n', k, type(k))

    print(data.get_quote_yahoo(symbol).columns)
    return pd.DataFrame.from_dict(df)