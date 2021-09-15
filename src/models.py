from typing import NamedTuple


class DividendDiscountParams(NamedTuple):
    net_income: float 
    growth_rate: float
    discount_rate: float
    shares_outstanding: float
    payout_ratio: float = 0.5


def get_divident_discount(p: DividendDiscountParams) -> float:
    divident_next_year = (p.net_income / p.shares_outstanding) * p.payout_ratio
    return divident_next_year / (p.discount_rate - p.growth_rate)
