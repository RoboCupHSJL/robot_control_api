from sensor_interface import SensorInterface
from sensor_msgs.msg import Imu
from webots_ros2_core.math.interpolation import interpolate_lookup_table


class IMUSensorInterface(SensorInterface):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._frame_id = self._name
        #self.__publisher = self.create_publisher(Imu, 'imu_sensor', 1)
        self._current_imu = None

    def _get_orientation(self):
        pass

    def _get_linear_accleration(self):
        pass

    def _get_angular_velocity(self):
        pass

    def publish(self):
        msg = self.read()
        self._current_imu = msg
        #self.__publisher.publish(msg)


    def read(self):
        
        msg = Imu()

        #msg.header.stamp = rclpy.now()
        msg.header.frame_id = self._frame_id

        raw_data = self._get_linear_accleration()
        if raw_data:
            msg.linear_acceleration.x = raw_data[0]
            msg.linear_acceleration.y = raw_data[1]
            msg.linear_acceleration.z = raw_data[2]

        raw_data = self._get_angular_velocity()
        if raw_data:
            msg.angular_velocity.x = raw_data[0]
            msg.angular_velocity.y = raw_data[1]
            msg.angular_velocity.z = raw_data[2]

        raw_data = self._get_orientation()
        if raw_data:
            msg.orientation.x = raw_data[0]
            msg.orientation.y = raw_data[1]
            msg.orientation.z = raw_data[2]
            msg.orientation.w = raw_data[3]

        return msg