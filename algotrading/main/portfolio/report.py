
class PositionReport(object):
    """Class that holds the information about the position used to generate a report"""

    def __init__(self):
        self.report_date = None
        self.symbol = None
        self.symbol_market_value = 0
        self.quantity = 0
        self.market_value = 0
        self.total_cost = 0
        self.gain_or_loss = 0


class PortfolioReport:
    """Holds data about a portfolio thats used to render a report"""

    def __init__(self):
        self.report_date = None
        self.position_reports = []
        self.total_cost = 0
        self.market_value = 0
        self.gain_or_loss = 0
