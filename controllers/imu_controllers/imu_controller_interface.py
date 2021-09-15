# TODO: add docs
from controllers import ControllerInterface


class ImuControllerInterface(ControllerInterface):
    """[summary]

    Args:
        ControllerInterface ([type]): [description]
    """
    def step(self):
        """[summary]
        """
        for imu in self.hardware_interfaces.values():
            imu.read()
