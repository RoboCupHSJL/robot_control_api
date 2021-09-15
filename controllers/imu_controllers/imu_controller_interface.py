# TODO: add docs
from controllers import ControllerInterface
from global_ import interactor


class ImuControllerInterface(ControllerInterface):
    """[summary]

    Args:
        ControllerInterface ([type]): [description]
    """
    def step(self):
        """[summary]
        """
        for imu in self.hardware_interfaces.values():
            interactor[imu.name] = imu.read()
