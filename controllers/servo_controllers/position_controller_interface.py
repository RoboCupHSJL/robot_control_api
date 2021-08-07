# TODO: add docs
import queue
from controllers import ControllerInterface


class PositionControllerInterface(ControllerInterface):
    """[summary]

    Args:
        ControllerInterface ([type]): [description]
    """
    def __init__(self, config):
        super().__init__(config)
        self._pos_queue = queue.Queue()

        self._servos = config.get('servos')

    def step(self):
        """[summary]
        """
        if not self._pos_queue.empty():
            servo_name, position = self._pos_queue.get()
            self.hardware_interfaces[servo_name].write(position)

    def set_position(self, servo_name, position):
        """[summary]

        Args:
            servo_name ([type]): [description]
            position ([type]): [description]
        """
        self._pos_queue.put([servo_name, position])
