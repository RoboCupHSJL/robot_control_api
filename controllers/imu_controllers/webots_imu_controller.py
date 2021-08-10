# TODO: add docs
from .imu_controller_interface import ImuControllerInterface
from hardware_interfaces.sensors.imu.webots_imu import WebotsIMU


class WebotsImuController(ImuControllerInterface):
    """[summary]

    Args:
        ImuControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent):
        super().__init__(name)

        self.agent = agent

        self._add_interface(WebotsIMU(name='imu', agent=agent))
