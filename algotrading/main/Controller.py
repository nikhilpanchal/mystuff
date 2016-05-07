from portfolio.PortfolioManager import PortfolioManager


class Controller:
    """Controller class that will orchestrate the various pieces of work"""

    def __init__(self):
        self.portfolio_manager = PortfolioManager()

    # def run_algo(self, algo_name):
    #     return algo_name

    def initialize_portfolio(self):
        """Fills it with positions obtained from user input"""
        '''For now assume the user input is to create a portfolio with cash and 2 positions'''
        self.portfolio_manager.add_cash(100000)
        self.portfolio_manager.add_position("IBM", 100, 134.3)
        self.portfolio_manager.add_position("GOOG", 100, 705.7)

    def get_portfolio_value(self):
        port_value = self.portfolio_manager.calculate_market_value()

        print("Portfolio value as of today: {}".format(port_value))

    def get_portfolio_return(self):
        port_return = self.portfolio_manager.calculate_return()

        print("Portfolio unrealized gain as of today {}".format(port_return))


if __name__ == '__main__':
    controller = Controller()
    controller.initialize_portfolio()
    controller.get_portfolio_value()
    controller.get_portfolio_return()

