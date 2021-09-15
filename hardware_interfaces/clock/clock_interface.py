# TODO: add docs
from abc import abstractmethod


class ClockInterface:
    """[summary]
    """
    def __init__(self, agent=None):
        self.__agent = agent

    @abstractmethod
    def now(self):
        """[summary]
        """
