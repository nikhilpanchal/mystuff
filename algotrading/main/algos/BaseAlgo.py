import abc


class BaseAlgo(abc.ABC):
    """Base class that every algorithm should extend from"""

    def __init__(self):
        super(BaseAlgo, self).__init__()
        self.name = "Base"
        pass

    @abc.abstractmethod
    def back_test(self, start_date, end_date):
        """The back test method must be implemented by all Algos"""
        raise NotImplementedError