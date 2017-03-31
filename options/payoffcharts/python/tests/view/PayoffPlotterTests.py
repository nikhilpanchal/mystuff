import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock

from view.graphview import PayoffPlotter


class PlotTests(TestCase):
    """Test cases for the PayoffPlotter class"""

    @patch("view.graphview.plt", autospec=True)
    def test_plot_payoff(self, plt):
        points = MagicMock(name="points")
        points.keys.return_value = [0, 1]
        points.values.return_value = [1, 0]

        payoff_plotter = PayoffPlotter()
        payoff_plotter.plot_payoff(points)

        self.assertEqual(points.keys.called, True, "X values are the keys of the dict")
        self.assertEqual(points.values.called, True, "Y values are the keys of the dict")

        plt.xlabel("Stock Price $")
        plt.ylabel("Return $")
        plt.title.assert_called_once_with("Option Strategy Payoff")
        plt.grid.assert_called_once_with(True)
        plt.axis.assert_called_once_with([0, 12, -10, 12])
        plt.plot.assert_called_once_with([0, 1], [1, 0], label="Payoff")
        plt.show.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
