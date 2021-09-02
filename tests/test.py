import yfinance as yf

msft = yf.Ticker("MSFT")

msft.balance_sheet
#msft.quarterly_balance_sheet