# TODO: add docs
from .imu_controller_interface import ImuControllerInterface
from hardware_interfaces.sensors.imu.webots_imu import WebotsIMU
from hardware_interfaces.sensors.imu.elsiros_imu import ElsirosIMU

class GeneralImuController(ImuControllerInterface):
    """[summary]

    Args:
        ImuControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode, config, clock):
        super().__init__(name, clock)

        self.agent = agent

        if mode == 'webots':
            self._add_interface(WebotsIMU(name='imu', agent=agent, config=config))
        elif mode == 'elsiros':
            self._add_interface(ElsirosIMU(name='imu_head', agent=agent, config=config, clock=clock))
            self._add_interface(ElsirosIMU(name='imu_body', agent=agent, config=config, clock=clock))
        else:
            # ADDITION OF CUSTOM HARDWARE INTERFACE
            pass
