from sensor_msgs.msg import Imu
from imu_sensor_interface import IMUSensorInterface
from controller import Accelerometer, InertialUnit, Gyro

class WebotsIMUHW(IMUSensorInterface):
    def __init__(self, name, robot):
        super().__init__(name)
        print(self._current_imu)
        self.robot = robot

        self.__accel = None
        self.__gyro = None
        self.__in_unit = InertialUnit('imu')
        self.__in_unit.enable(100)

    def start(self):
        try:
            self.__in_unit.enable()
        except:
            self._status = 'disabled'
            return

        self._status = 'enabled'

    def _get_orientation(self):
        if self.__in_unit:
            return self.__in_unit.getQuaternion()
        else:
            return None


    def _get_linear_accleration(self):
        if self.__accel:
            return self.__accel.getValues()
        else:
            return None
        

    def _get_angular_velocity(self):
        if self.__gyro:
            return self.__gyro.getValues()
        else:
            return None
