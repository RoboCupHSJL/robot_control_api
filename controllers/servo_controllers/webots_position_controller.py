# TODO: add docs
from hardware_interfaces.actuators.servo.webots_servo import WebotsServo
from .position_controller_interface import PositionControllerInterface


class WebotsPositionController(PositionControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, config, robot):
        super().__init__(config)

        self.robot = robot

        for servo_config in self._servos.items():
            self._add_interface(WebotsServo(servo_config, robot))
