from imu_controller_interface import ImuControllerInterface
from hardware_interfaces import WebotsIMU


class WebotsImuController(ImuControllerInterface):
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        self._add_interface(WebotsIMU(name='Webots_IMU', robot=robot))

    def step(self):
        super().step()
