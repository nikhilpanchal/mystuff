from unittest import TestCase
from unittest.mock import MagicMock, patch, call

from calculators.longputstrategy import LongPutStrategy
from model.optionleg import OptionLeg
from payoffcalculator import PayOffCalculator


class PayOffCalculatorTest(TestCase):

    def test_register_strategy(self):
        calc = PayOffCalculator()
        strategy = LongPutStrategy()

        calc.register_strategy(strategy)

        self.assertEqual(calc.strategy_map[strategy.STRATEGY_NAME],
                         strategy,
                         "The strategy must be registered in the strategy map")

    @patch("payoffcalculator.LongPutStrategy", autospec=True)
    @patch("payoffcalculator.LongCallStrategy", autospec=True)
    def test_calculate(self, longCallMock, longPutMock):
        longCallMock.calculate_payoff.return_value = 10
        longPutMock.calculate_payoff.return_value = 20

        legs = [
            OptionLeg("Buy", "Call", 0, 0),
            OptionLeg("Buy", "Put", 0, 0)
        ]

        calc = PayOffCalculator()
        calc.strategy_map = {
            legs[0].get_strategy(): longCallMock,
            legs[1].get_strategy(): longPutMock
        }

        payoff = calc.calculate(legs)

        # Check that the legs resolved to the right strategy
        # and that the calls on the strategies were made
        self.assertEqual(longCallMock.mock_calls[0], call.calculate_payoff(legs[0], 0),
                         "The long call strategy must be called with the underlying price of 0")
        self.assertEqual(longCallMock.mock_calls[50], call.calculate_payoff(legs[0], 50),
                         "The long call strategy must be called with the underlying price of 50")
        self.assertEqual(longCallMock.mock_calls[100], call.calculate_payoff(legs[0], 100),
                         "The long call strategy must be called with the underlying price of 100")
        self.assertEqual(longPutMock.mock_calls[0], call.calculate_payoff(legs[1], 0),
                         "The long put strategy must be called with the underlying price of 0")
        self.assertEqual(longPutMock.mock_calls[100], call.calculate_payoff(legs[1], 100),
                         "The long put strategy must be called with the underlying price of 100")

        self.assertEqual(payoff[0], 30, "The calculator must sum the payoff of the strategies")
        self.assertEqual(payoff[100], 30, "The calculator must sum the payoff of the strategies")