# TODO: add docs
from hardware_interfaces.actuators.servo.elsiros_servo import ElsirosServo
from .position_controller_interface import PositionControllerInterface


class ElsirosPositionController(PositionControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, config, agent):
        super().__init__(name, config)

        self.__agent = agent

        for servo_config in self._servos.items():
            self._add_interface(ElsirosServo(servo_config[0], agent))
