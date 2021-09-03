# TODO: add docs
from .imu_controller_interface import ImuControllerInterface
from hardware_interfaces.sensors.imu.webots_imu import WebotsIMU
from hardware_interfaces.sensors.imu.elsiros_imu import ElsirosIMU

class GeneralImuController(ImuControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode):
        super().__init__(name)

        self.agent = agent

        if mode == 'webots':
            self._add_interface(WebotsIMU(name='imu', agent=agent))
        elif mode == 'elsiros':
            self._add_interface(ElsirosIMU(name='imu_head', agent=agent))
            self._add_interface(ElsirosIMU(name='imu_body', agent=agent))
        else:
            # ADDITION OF CUSTOM HARDWARE INTERFACE
            pass
