# TODO: add docs
from controllers import ControllerInterface
from communication import interactor


class ImuControllerInterface(ControllerInterface):
    """[summary]

    Args:
        ControllerInterface ([type]): [description]
    """
    def step(self):
        """[summary]
        """
        for imu in self.hardware_interfaces.values():
            interactor.push_message(imu.name, imu.read())
