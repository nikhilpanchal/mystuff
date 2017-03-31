from unittest import TestCase
from model.optionleg import OptionLeg


class OptionLegTest(TestCase):
    def setUp(self):
        self.option_leg = OptionLeg("Buy", "Call", 100, 5)

    def test_initialization(self):
        self.assertEqual(self.option_leg.side, "Buy")
        self.assertEqual(self.option_leg.type, "Call")
        self.assertEqual(self.option_leg.strike, 100)
        self.assertEqual(self.option_leg.price, 5)

    def test_get_strategy(self):
        self.assertEqual(self.option_leg.get_strategy(), "Buy_Call")

    def test_str(self):
        option_str = str(self.option_leg)
        self.assertEqual("Option Leg: Side: Buy, Type: Call, Strike: 100, Price: 5, \
            Strategy Buy_Call", option_str)