# TODO: add docs
from abc import ABCMeta, abstractmethod


class HardwareInterface:
    __metaclass__ = ABCMeta
    """[summary]
    """
    def __init__(self, name):

        """[summary]
        """
        self._name = name
        self._status = 'disabled'

    @abstractmethod
    def get_param(self, param_name):
        """[summary]
        """

    @abstractmethod
    def start(self):
        """[summary]
        """

    @abstractmethod
    def stop(self):
        """[summary]
        """

    @property
    def name(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._name

    @property
    def status(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._status
