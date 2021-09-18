# TODO: add docs
from .imu_controller_interface import ImuControllerInterface
from hardware_interfaces.sensors.imu.webots_imu import WebotsIMU
from hardware_interfaces.sensors.imu.elsiros_imu import ElsirosIMU
from communication import interactor

class GeneralImuController(ImuControllerInterface):
    """[summary]

    Args:
        ImuControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode, hw_class, config, clock):
        super().__init__(name, clock)

        self.agent = agent

        if mode == 'webots':
            self._add_interface(WebotsIMU(name='imu', agent=agent, config=config, clock=clock))

        elif mode == 'elsiros':
            self._add_interface(ElsirosIMU(name='imu_head', agent=agent, config=config, clock=clock))
            self._add_interface(ElsirosIMU(name='imu_body', agent=agent, config=config, clock=clock))
        else:
            try:
                self._add_interface(hw_class(name='imu', agent=agent, config=config, clock=clock))
            except:
                raise Exception('Incorrect IMU class')
