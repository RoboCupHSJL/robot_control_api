from imu_controller_interface import ImuControllerInterface
from webots_imu_hw import WebotsIMUHW
from controller import Accelerometer, InertialUnit, Gyro


class WebotsImuController(ImuControllerInterface):
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        self._add_interface(WebotsIMUHW(name='Webots_IMU', robot=robot))

    def step(self):
        super().step()
