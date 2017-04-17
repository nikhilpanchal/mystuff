from unittest import TestCase
from unittest.mock import patch, call

from controller import Controller


class ControllerTest(TestCase):

    @patch("controller.LongUnderlying")
    @patch("controller.PayoffPlotter")
    @patch("controller.PayOffCalculator", autospec=True)
    def test_initialization(self, calculator,
                            plotter,
                            longUnderlying):
        calc_instance = calculator.return_value
        strat_instance = longUnderlying.return_value

        Controller()

        self.assertTrue(calculator.called, "An instance of calculator must be created")
        self.assertTrue(plotter.called, "An instance of the plotter must be created")
        self.assertEqual(calc_instance.mock_calls[4],
                         call.register_strategy(strat_instance))

    @patch("controller.PayoffPlotter", autospec=True)
    @patch("controller.PayOffCalculator", autospec=True)
    def test_get_strategy_payoff(self, calculator, plotter):
        self.controller = Controller()

        legs = []
        payoff = {0: 1}

        # Methods on the instances are called, so create method mocks
        # on the instances.
        calc_instance = calculator.return_value
        calc_instance.calculate.return_value = payoff
        plot_instance = plotter.return_value

        self.controller.get_strategy_payoff(legs)

        calc_instance.calculate.assert_called_once_with(legs)
        plot_instance.plot_payoff.assert_called_once_with(payoff)

