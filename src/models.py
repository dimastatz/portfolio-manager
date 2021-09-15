import random
from typing import List, NamedTuple

class Model:
    def __init__(self, name: str):
        self.name = name
    
    def run(self) -> str:
        raise Exception('Run is not implemented in Abstract Model')


class RandomModel(Model):
    def __init__(self, name: str):
        super().__init__(name)

    def run(self) -> str:
        return 'Buy' if bool(random.getrandbits(1)) else 'Sell'


def get_models() -> List[Model]:
    return [RandomModel('Model_1'), RandomModel('Model_2'), RandomModel('Model_3')]
       

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

    def

def get_divident_discount(p: DividendDiscountParams) -> float:
    divident_next_year = (p.net_income / p.shares_outstanding) * p.payout_ratio
    return divident_next_year / (p.discount_rate - p.growth_rate)
