# TODO: add docs
from abc import abstractmethod
from hardware_interfaces import HardwareInterface


class SensorInterface(HardwareInterface):
    """[summary]
    """

    @abstractmethod
    def read(self):
        """[summary]
        """

    def start(self):
        self.status = "enabled"

    def stop(self):
        self.status = "disabled"
