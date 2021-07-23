from device_imu_hw import BNO055IMUHW
from imu_controller_interface import ImuControllerInterface
from bno_imu_hw import BNO055IMUHW
from webots_ros2_core.webots_node import WebotsNode
from controller import Accelerometer, InertialUnit, Gyro


class KondoAtomImuController(ImuControllerInterface):
    def __init__(self):
        super().__init__()

        # for now like this
        self.__devices = None

        self._add_interface(BNO055IMUHW(name='head_imu', device=None))
        self._add_interface(RCB4(name='body_imu', device=None))
