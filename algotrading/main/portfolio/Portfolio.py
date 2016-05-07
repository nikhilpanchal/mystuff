from datetime import date
from datetime import timedelta


class Portfolio:
    '''The main portfolio class. Exposes functions to view positions, performance, activity. Handles trades made in it
    to keep cash balances up to date based on the activity performed in the portfolio'''

    def __init__(self):
        # Positions in the portfolio, keyed by the symbol
        self.positions = {}

        # The amount of cash in the portfolio
        self.cash = 0

        # The market value of the portfolio
        self.market_value = 0

        # The date at which the market value was calculated
        self.market_value_date = None
        

    def __get_market_value_on_date(self, date):
        """Calculates the market value of the entire portfolio based on market prices of positions on a given date"""
        pass

    def add_position(self, position):
        pass

    def sell_position(self, position):
        pass

    def get_market_value(self):
        return self.__get_market_value_on_date(date.today())

    def get_cash_balance(self):
        pass

    def consume_order(self, order):
        """Updates the positions in the portfolio with the details of the order.
        Will only work with executed orders."""
        pass

    def get_value_over_time(self, from_date, to_date=date.today()):
        """Returns a dictionary of date and portfolio values where the dates range from from_date to to_date.
        to_date defaults to today if not provided."""
        performance = {}

        i = 0
        date_i = from_date
        while date_i < to_date:
            date_i = from_date + timedelta(i)
            i += 1
            performance[date_i] = 1