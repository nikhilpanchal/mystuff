from calculators.longputstrategy import LongPutStrategy
from model.optionleg import OptionLeg
from unittest import TestCase


class LongPutStrategyTest(TestCase):
    def setUp(self):
        super().setUp()

        self.strat = LongPutStrategy()
        self.leg = OptionLeg("Buy", "Put", 100, 5)

    def test_calculate_payoff(self):
        """The put is in the money"""
        payoff = self.strat.calculate_payoff(self.leg, 55)
        self.assertEqual(payoff, 40, "The payoff will be the difference between the strike and the current stock price")

    def test_payoff_out_of_the_money(self):
        """The scenario for when the put is out of the money"""
        payoff = self.strat.calculate_payoff(self.leg, 105)
        self.assertEqual(payoff, -5, "If the stock goes up the holder of the put loses the price of the put")