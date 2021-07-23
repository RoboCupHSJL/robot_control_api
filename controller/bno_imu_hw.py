from sensor_msgs.msg import Imu
from rclpy.qos import QoSReliabilityPolicy, qos_profile_sensor_data
from imu_sensor_interface import IMUSensorInterface

class DeviceIMUHW(IMUSensorInterface):
    def __init__(self, name, device):

        self.device = device

    def start(self):
        try:
            self.__in_unit.enable()
        except:
            self._status = 'disabled'
            return

        self._status = 'enabled'

    def _get_orientation(self):
        pass

    def _get_linear_accleration(self):
        pass

    def _get_angular_velocity(self):
        pass