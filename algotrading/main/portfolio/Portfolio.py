from datetime import date
from datetime import timedelta


class Portfolio:
    """The main portfolio class. Exposes functions to view positions, performance, activity. Handles trades made in it
    to keep cash balances up to date based on the activity performed in the portfolio"""

    def __init__(self):
        # Positions in the portfolio, keyed by the symbol
        self.positions = {}

        # The amount of cash in the portfolio
        self.cash = 0

        # The total cost of the portfolio
        self.total_cost = 0
