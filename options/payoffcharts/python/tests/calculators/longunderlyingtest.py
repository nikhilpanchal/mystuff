from unittest import TestCase

from calculators.longunderlying import LongUnderlying
from model.optionleg import OptionLeg


class LongUnderlyingTest(TestCase):
    """Test Cases for the Long underlying strategy"""

    def test_calculate_payoff(self):
        strat = LongUnderlying()
        leg = OptionLeg("Buy", "Stock", 0, 100)

        payoff = strat.calculate_payoff(leg, 120)

        self.assertEqual(payoff, 20, "The payoff is the difference between the current price and the purchase price")