import unittest

from ..main.Controller import Controller


class ControllerTestCase(unittest.TestCase):
    '''Test case class for the Controller'''

    def setUp(self):
        self.controller = Controller()

    def test_run_algo(self):
        self.assertEqual(self.controller.run_algo("MovingAverage"), "MovingAverage")

    def test_run_algo2(self):
        self.assertEqual(self.controller.run_algo("SecondCase"), "SecondCase")


if __name__ == '__main__':
    unittest.main()
