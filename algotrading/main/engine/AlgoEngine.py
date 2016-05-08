class AlgoEngine:
    """Class that holds the set of algorithms and runs them when requested"""

    def __init__(self):
        self.algo_map = {}
        pass

    def register_algorithm(self, algo):
        pass

    def back_test_algo(self, algo_name, start_date, end_date):
        algo = self.algo_map.get(algo_name)

        algo.back_test(start_date, end_date)
