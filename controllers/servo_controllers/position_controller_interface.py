# TODO: add docs
import queue
from controllers import ControllerInterface
from global_ import interactor


class PositionControllerInterface(ControllerInterface):
    """[summary]

    Args:
        ControllerInterface ([type]): [description]
    """
    def __init__(self, name, config, clock):
        super().__init__(name, clock)
        self._pos_queue = queue.Queue()

        self._servos = config.get('servo_controller').get('servos')

    def step(self):
        """[summary]
        """
        for servo in self.hardware_interfaces.values():
            interactor[servo.name] = servo.read()
        #if not self._pos_queue.empty():
        #    servo_name, position = self._pos_queue.get()
        #    self.hardware_interfaces[servo_name].write(position)
        if not interactor.cmd_empty:
            cmd_msg = interactor.get_message('servo_cmd')
            for servo_name, value in cmd_msg.frame.items():
                if servo_name in self.hardware_interfaces:
                    self.hardware_interfaces[servo_name].write(value)

    def set_position(self, servo_name, position):
        """[summary]

        Args:
            servo_name ([type]): [description]
            position ([type]): [description]
        """
        #self._pos_queue.put([servo_name, position])
        pass
