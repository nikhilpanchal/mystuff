
from datetime import date
from .PositionType import PositionType
from .PositionType import AssetClass


class Position:
    """Represents an individual position in the portfolio"""

    def __init__(self, symbol, quantity, unit_price, position_type=PositionType.LONG, asset_class=AssetClass.STOCK):
        self.position_type = position_type
        self.asset_class = asset_class
        self.symbol = None

        '''Price paid for a single unit of the underlying symbol to acquire this position'''
        self.unit_price = 0

        '''Number of units of the symbol in this position'''
        self.quantity = 0

        '''Market value of the underlying and the overall position'''
        self.underlying_market_value = 0
        self.market_value = 0
        self.market_value_date = None

        '''Price paid to acquire this position'''
        self.total_cost = 0

        '''Gain/Loss'''
        self.gain_or_loss = 0

    def __str__(self):
        return repr(self.type)

    def set_market_value(self, underlying_market_price):
        """Updates the market value related fields based on the newly provided market price"""
        self.underlying_market_value = underlying_market_price
        self.market_value = self.quantity * self.underlying_market_price
        self.market_value_date = date.today()

    def __update_metrics(self):
        """Update all the inner metrics of the position. Called when quantity is changed or new market price obtained"""
        self.total_cost = self.unit_price * self.quantity
        self.gain_or_loss = self.market_value - self.total_cost
    
    def add_to_holding(self, quantity):
        """Quantity added to this position"""
        self.quantity += quantity

    def reduce_holding(self, quantity):
        """Quantity is sold from this position"""
        self.quantity -= quantity








