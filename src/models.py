#
class DividentDiscountModel:
    def __init__(self) -> None:
        self.share_price: float
        self.earning_per_share: float
        self.book_value_per_share: float
        self.sales_per_share: float
        self.pe_ratio: float
        self.pb_ratio: float
        self.ps_ratio: float
        self.net_income: float
        self.shares_outstanding: float

        # we asume that 50% of net income 
        # will be used to pay a divident to 
        # shareholders 
        self.payout_ratio: float = 50
        self.growth_rate: float
        self.discount_rate: float

        # (net_income / number_of_shares) * payout_ratio
        self.divident_next_year = (self.net_income / self.shares_outstanding) * self.payout_ratio


    def calculate(self) -> float:
        self.divident_next_year / (self.discount_rate - self.growth_rate)