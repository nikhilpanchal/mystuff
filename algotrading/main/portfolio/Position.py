from .PortfolioEnums import AssetClass


class Position:
    """Represents an individual position in the portfolio"""

    def __init__(self, symbol, quantity, cost, asset_class=AssetClass.EQUITY):
        """Position must be created with a minimum of the symbol, the quantity and the total cost"""
        self.asset_class = asset_class
        self.symbol = symbol

        '''Number of units of the symbol in this position'''
        self.quantity = quantity

        self.average_unit_cost = cost

        '''Price paid to acquire (all units of) this position'''
        self.total_cost = self.quantity * self.cost

        self.symbol_market_value = 0
        self.market_value = 0
        self.market_value_date = None



    def __str__(self):
        return repr(self.type)

    def calculate_market_value(self, underlying_market_price):
        """Calculates the market value of the overall position for the provided market price of the symbol"""
        return self.quantity * underlying_market_price

    def calculate_return(self, underlying_market_price):
        """Calculates the return (gain/loss) on this position for the provided market price of the symbol"""
        market_value = self.calculate_market_value(underlying_market_price)
        return market_value - self.total_cost

    def increase(self, quantity, unit_cost):
        """Updates the numbers for an increase of this position"""
        '''Calculate the new average unit cost for the position'''
        self.average_unit_cost = (self.average_unit_cost * self.quantity + quantity * unit_cost) \
                                     / \
                                     (self.quantity + quantity)

        '''Set the new total cost of the position based on the new quantity and new average unit cost'''
        self.quantity += quantity
        self.total_cost += self.average_unit_cost * quantity

    def decrease(self, quantity):
        """Updates the names for a decrease of this position"""
        self.quantity -= quantity

        self.total_cost = self.quantity * self.average_unit_cost





