from .Portfolio import Portfolio
from .Position import Position
from .report import PortfolioReport, PositionReport
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
            position = Position(symbol, quantity, unit_cost)

            '''Add to the portfolio'''
            self.portfolio.positions[symbol] = position
        else:
            '''If the portfolio has a position for this symbol, amend it'''
            position = self.portfolio.positions[symbol]

            '''Add the increment to the position'''
            position.increase(quantity, unit_cost)

    def sell_position(self, symbol, quantity, unit_sale_price):
        if symbol not in self.portfolio.positions:
            '''Confirm that the position exists. If not raise an exception'''
            raise Exception("No position in portfolio for symbol {}".format(symbol))

        position = self.portfolio.positions[symbol]

        if position.quantity < quantity:
            '''Check whether the position has enough units to sell'''
            raise Exception("The portfolio does not have {} units of the symbol {} to see".format(quantity, symbol))

        '''Reduce the quantity and total cost of the position based on the amount sold'''
        position.decrease(quantity)

        '''If the position quantity is zero, remove it from the portfolio'''
        if position.quantity == 0:
            self.portfolio.positions.pop(symbol)

        '''Add the proceeds of the sale to the cash'''
        self.portfolio.cash += quantity*unit_sale_price

    def calculate_market_value(self, market_value_date=date.today()):
        """Returns the market value of the portfolio, by summing up the market value of all of its positions"""
        portfolio_market_value = self.portfolio.cash

        for position_entry in self.portfolio.positions.items():
            symbol = position_entry[0]
            position = position_entry[1]

            '''Get market price for this symbol for the date specified'''
            market_price = MarketData.get_stock_price(symbol, market_value_date)

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

            '''Get the market price for the symbol for the date specified'''
            market_price = MarketData.get_stock_price(symbol, date)

            '''Calculate the market value of this position'''
            position_return = position.calculate_return(market_price)

            '''Add it to the portfolio market value'''
            portfolio_return += position_return

        return portfolio_return

    def get_portfolio_report(self, report_date=date.today()):
        """Returns a report object for the portfolio that will show all of the metrics of the portfolio.
        Metrics include: Market Value, Gain/Loss"""

        portfolio_report = PortfolioReport()
        portfolio_report.report_date = report_date
        portfolio_report.market_value = self.portfolio.cash

        for position in self.portfolio.positions.items():
            symbol = position[0]
            position = position[1]

            '''Get the market price for the symbol for the given date'''
            symbol_market_value = MarketData.get_stock_price(symbol, report_date)

            '''Calculate the market value for this position'''
            position_market_value = position.calculate_market_value(symbol_market_value)

            '''Calculate the return for the position for this symbol market value'''
            position_return = position.calculate_return(symbol_market_value)

            '''Create the position report object with the retrieved data filled in'''
            position_report = PositionReport()
            position_report.report_date = report_date
            position_report.symbol = symbol
            position_report.symbol_market_value = symbol_market_value
            position_report.quantity = position.quantity
            position_report.market_value = position_market_value
            position_report.total_cost = position.total_cost
            position_report.gain_or_loss = position_return

            portfolio_report.position_reports.append(position_report)

            '''Update the portfolio numbers'''
            portfolio_report.market_value += position_market_value
            portfolio_report.total_cost += position.total_cost

        '''Calculate the portfolio gain or loss'''
        portfolio_report.gain_or_loss = portfolio_report.market_value - portfolio_report.total_cost

        return portfolio_report
