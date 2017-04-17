from .basestrategy import BaseStrategy


class ShortUnderlyingStrategy(BaseStrategy):
    """The Payoff Strategy for going short a stock"""
    STRATEGY_NAME = "Sell_Stock"

    def __init__(self):
        super().__init__()

    def calculate_payoff(self, leg, stock_price):
        return leg.price - stock_price
