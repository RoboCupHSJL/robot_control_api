# TODO: add docs
from abc import abstractmethod
from hardware_interfaces.hardware_interface import HardwareInterface


class ActuatorInterface(HardwareInterface):
    """[summary]
    """

    @abstractmethod
    def read(self):
        """[summary]
        """

    def write(self, message):
        """[summary]

        Args:
            message ([type]): [description]
        """

    def start(self):
        self.status = "enabled"

    def stop(self):
        self.status = "disabled"
