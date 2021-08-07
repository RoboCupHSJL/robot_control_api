# TODO: add docs
from hardware_interfaces.actuators.servo.elsiros_servo import ElsirosServo
from .position_controller_interface import PositionControllerInterface


class ElsirosPositionController(PositionControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, config, agent):
        super().__init__(config)

        self.__agent = agent

        for servo_name in self._servo_id_list:
            self._add_interface(ElsirosServo(servo_name, agent))
