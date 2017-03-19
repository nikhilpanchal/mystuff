import unittest

from calculators.shortunderlyingstrategy import ShortUnderlyingStrategy
from model.optionleg import OptionLeg


class ShortUnderlyingTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.short_underlying = ShortUnderlyingStrategy()

    def test_calculate(self):
        leg = OptionLeg("Sell", "Stock", None, price=50)

        payoff = self.short_underlying.calculate_payoff(leg, 75)

        self.assertEqual(payoff, -25, "The payoff is the difference between the shorted price and the underlying")