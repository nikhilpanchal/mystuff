import unittest
from calculators.longcallstrategy import LongCallStrategy
from model.optionleg import OptionLeg


class LongCallStrategyTest(unittest.TestCase):

    STRATEGY_NAME = "Buy_Stock"

    def setUp(self):
        super().setUp()
        self.long_call = LongCallStrategy()

    def test_calculate_payoff(self):
        leg = OptionLeg("Buy", "Call", 100, 5.0)

        # Run the test
        pay_off = self.long_call.calculate_payoff(leg, 150)

        self.assertEqual(pay_off, 45, "The payoff will be the difference between the stock price and the strike")


