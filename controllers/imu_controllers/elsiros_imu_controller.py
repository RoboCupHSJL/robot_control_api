# TODO: add docs
from .imu_controller_interface import ImuControllerInterface
from hardware_interfaces.sensors import ElsirosIMU


class ElsirosImuController(ImuControllerInterface):
    """[summary]

    Args:
        ImuControllerInterface ([type]): [description]
    """
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        self._add_interface(ElsirosIMU(name='imu', robot=robot))
