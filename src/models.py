from typing import NamedTuple

class DividentDiscountParams(NamedTuple):
    net_income: float 
    growth_rate: float
    discount_rate: float
    shares_outstanding: float
    payout_ratio: float = 50


def get_divident_discount(p: DividentDiscountParams) -> float:
    divident_next_year = (p.net_income / p.shares_outstanding) * p.payout_ratio
    return divident_next_year / (p.discount_rate - p.growth_rate)