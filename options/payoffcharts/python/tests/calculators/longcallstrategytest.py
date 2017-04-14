import unittest
from calculators.longcallstrategy import LongCallStrategy
from model.optionleg import OptionLeg


class LongCallStrategyTest(unittest.TestCase):

    STRATEGY_NAME = "Buy_Stock"

    def setUp(self):
        self.long_call = LongCallStrategy()

    def test_calculate_payoff(self):
        leg = OptionLeg("Buy", "Call", 100, 5.0)

        # Run the test
        pay_off = self.long_call.calculate_payoff(leg, 150)

        self.assertEqual(pay_off, 45, "The payoff will be the difference between the stock price and the strike")

    def test_out_of_the_money_call(self):
        leg = OptionLeg("Buy", "Call", 100, 5.0)

        pay_off = self.long_call.calculate_payoff(leg, 90)

        self.assertEqual(pay_off, -5.0, "The payoff will be the loss on the price paid with no upside")


