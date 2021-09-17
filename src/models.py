import random
import pandas as pd
from typing import List, NamedTuple
from pandas.core.frame import DataFrame


class Model:
    def __init__(self, name: str):
        self.name = name

    def run(self, stock: str) -> str:
        raise Exception('Run is not implemented in Abstract Model')


class RandomModel(Model):
    def __init__(self, name: str):
        super().__init__(name)

    def run(self, stock: str) -> str:
        return 'Buy' if bool(random.getrandbits(1)) else 'Sell'


class DividendDiscountParams(NamedTuple):
    net_income: float
    growth_rate: float
    discount_rate: float
    shares_outstanding: float
    payout_ratio: float = 0.5


class DividendDiscountParams(Model):
    def __init__(self, name: str, params: DividendDiscountParams):
        super().__init__(name)
        self.params = params


def get_divident_discount(p: DividendDiscountParams) -> float:
    divident_next_year = (p.net_income / p.shares_outstanding) * p.payout_ratio
    return divident_next_year / (p.discount_rate - p.growth_rate)


def get_models() -> List[Model]:
    return [
        RandomModel('Model_1'),
        RandomModel('Model_2'),
        RandomModel('Model_3'),
        RandomModel('Model_4')
    ]


def evaluate_portfolio(portfolio: List[str]) -> DataFrame:
    data = {'Stock': portfolio}
    for model in get_models():
        data[model.name] = [model.run(p) for p in portfolio]
        
    return pd.DataFrame.from_dict(data=data)
