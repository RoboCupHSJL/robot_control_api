from actuator_interface import ActuatorInterface
from std_msgs.msg import Float32
import rclpy

class ServoActuatorInterface(ActuatorInterface):
    def __init__(self) -> None:
        super().__init__()
        self._frame_id = self._name
        self.__publisher = self.create_publisher(Float32, 'servo', 1)

    def _get_position(self):
        pass

    def _set_position(self, msg):
        pass

    def read(self):

        msg = Float32()

        msg.header.stamp = rclpy.now()
        msg.header.frame_id = self._frame_id
        msg.value = self._get_position()

        return msg

    def write(self, msg):
        return self._set_position(msg)

    def publish(self):
        msg = self.read()
        self.__publisher.publish(msg)