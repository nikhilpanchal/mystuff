from .Portfolio import Portfolio
from .Position import Position
from marketdata.MarketData import MarketData

from datetime import date


class PortfolioManager:
    """Manages the portfolio. Exposes functions that a typical portfolio manager would perform on any portfolio"""
    def __init__(self):
        self.portfolio = Portfolio()

    def add_cash(self, amount):
        self.portfolio.cash += amount

    def withdraw_cash(self, amount):
        self.portfolio.cash -= amount

    def add_position(self, symbol, quantity, unit_cost):
        position_cost = quantity*unit_cost

        '''Check that the portfolio has cash to cover this addition'''
        if self.portfolio.cash < position_cost:
            raise Exception("The portfolio doesn't have enough cash to add this position")

        '''Reduce the cash by the position_cost amount'''
        self.portfolio.cash -= position_cost

        if symbol not in self.portfolio.positions:
            '''If the symbol doesnt exist in the portfolio create a new position for it'''
            position = Position(symbol, quantity, position_cost)

            '''Add to the portfolio'''
            self.portfolio.positions[symbol] = position
        else:
            '''If the portfolio has a position for this symbol, amend it'''
            position = self.portfolio.positions[symbol]
            position.quantity += quantity
            position.cost += position_cost

    def sell_position(self, symbol, quantity, unit_sale_price):
        if symbol not in self.portfolio.positions:
            '''Confirm that the position exists. If not raise an exception'''
            raise Exception("No position in portfolio for symbol {}".format(symbol))

        position = self.portfolio.positions[symbol]

        '''Reduce the quantity of the position by the amount sold'''
        position.quantity -= quantity

        '''Add the proceeds of the sale to the cash'''
        self.portfolio.cash += quantity*unit_sale_price

    def calculate_market_value(self, date=date.today()):
        """Returns the market value of the portfolio, by summing up the market value of all of its positions"""
        portfolio_market_value = self.portfolio.cash

        for position_entry in self.portfolio.positions.items():
            symbol = position_entry[0]
            position = position_entry[1]

            '''Get market price for this symbol for the date specified'''
            market_price = MarketData.get_stock_price(symbol, date)

            '''Calculate the market value of this position'''
            position_market_value = position.calculate_market_value(market_price)

            '''Add it to the portfolio market value'''
            portfolio_market_value += position_market_value

        return portfolio_market_value

    def calculate_return(self, date=date.today()):
        """Returns the unrealized gain or loss of this portfolio as of the given date"""
        portfolio_return = 0

        for position in self.portfolio.positions.items():
            symbol = position[0]
            position = position[1]

            '''Get the market prive for the symbol for the date specified'''
            market_price = MarketData.get_stock_price(symbol, date)

            '''Calculate the market value of this position'''
            position_return = position.calculate_return(market_price)

            '''Add it to the portfolio market value'''
            portfolio_return += position_return

        return portfolio_return



