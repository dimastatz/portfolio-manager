from abc import abstractclassmethod


from pandas.core.frame import DataFrame

class StockDataReader:
    @abstractclassmethod
    def read_stock_values() -> bool:
        pass

    @abstractclassmethod
    def read_stock_financials() -> bool:
        pass


class StockAnalysisModel:  
    @abstractclassmethod
    def get_buy_signal() -> bool:
        pass


class DiscountedCashFlowModel(StockAnalysisModel):
    def __init__(self, symbol: str, reader: StockDataReader):
        super().__init__()
        self.symbol = symbol
        self.reader = reader
    
    def get_buy_signal() -> bool:
        pass
