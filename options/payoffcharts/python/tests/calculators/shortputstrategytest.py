from unittest import TestCase

from calculators.shortputstrategy import ShortPutStrategy
from model.optionleg import OptionLeg


class ShortPutStrategyTest(TestCase):
    """Test cases for the short put strategy"""

    def setUp(self):
        self.strat = ShortPutStrategy()
        self.leg = OptionLeg("Sell", "Put", 100, 5)

    def test_calculate_payoff(self):
        """When the put is in the money"""
        payoff = self.strat.calculate_payoff(self.leg, 80)
        self.assertEqual(-15, payoff, "The payoff would be the difference between the ")

    def test_out_of_the_money(self):
        """When the put is out of the money"""
        payoff = self.strat.calculate_payoff(self.leg, 130)
        self.assertEqual(5, payoff, "The payoff is the sale price of the put")
