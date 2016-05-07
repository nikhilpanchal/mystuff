from .PortfolioEnums import AssetClass


class Position:
    """Represents an individual position in the portfolio"""

    def __init__(self, symbol, quantity, cost, asset_class=AssetClass.EQUITY):
        """Position must be created with a minimum of the symbol, the quantity and the total cost"""
        self.asset_class = asset_class
        self.symbol = symbol

        '''Number of units of the symbol in this position'''
        self.quantity = quantity

        '''Price paid to acquire (all units of) this position'''
        self.total_cost = cost

    def __str__(self):
        return repr(self.type)

    def calculate_market_value(self, underlying_market_price):
        """Calculates the market value of the overall position for the provided market price of the symbol"""
        return self.quantity * underlying_market_price

    def calculate_return(self, underlying_market_price):
        """Calculates the return (gain/loss) on this position for the provided market price of the symbol"""
        market_value = self.calculate_market_value(underlying_market_price)

        return market_value - self.total_cost





