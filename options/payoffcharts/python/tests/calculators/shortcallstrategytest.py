from unittest import TestCase

from calculators.shortcallstrategy import ShortCallStrategy
from model.optionleg import OptionLeg


class ShortCallStrategyTest(TestCase):

    def setUp(self):
        self.strat = ShortCallStrategy()
        self.leg = OptionLeg("Sell", "Call", 100, 5)

    def test_calculate_payoff(self):
        payoff = self.strat.calculate_payoff(self.leg, 90)
        self.assertEqual(5, payoff, "The payoff is the sale price of the call option")

    def test_out_of_the_money(self):
        payoff = self.strat.calculate_payoff(self.leg, 120)
        self.assertEqual(-15,
                         payoff,
                         "The payoff is the difference between the stock price and the strike net the sale price")
