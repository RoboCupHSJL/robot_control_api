# TODO: add docs
from .position_controller_interface import PositionControllerInterface
from hardware_interfaces.actuators import ElsirosServo


class ElsirosPositionController(PositionControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, robot):
        super().__init__(name)

        self.robot = robot

        for servo_name in self._servo_id_list:
            self._add_interface(ElsirosServo(servo_name, robot))