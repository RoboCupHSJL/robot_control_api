# TODO: add docs
from imu_controller_interface import ImuControllerInterface
from hardware_interfaces.sensors import WebotsIMU


class WebotsImuController(ImuControllerInterface):
    """[summary]

    Args:
        ImuControllerInterface ([type]): [description]
    """
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        self._add_interface(WebotsIMU(name='imu', robot=robot))
