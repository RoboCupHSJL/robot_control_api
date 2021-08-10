# TODO: add docs
from .imu_controller_interface import ImuControllerInterface
from hardware_interfaces.sensors.imu.elsiros_imu import ElsirosIMU


class ElsirosImuController(ImuControllerInterface):
    """[summary]

    Args:
        ImuControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent):
        super().__init__(name)

        self.agent = agent

        self._add_interface(ElsirosIMU(name='imu', agent=agent))
