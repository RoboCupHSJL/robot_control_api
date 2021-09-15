# TODO: add docs
from .position_controller_interface import PositionControllerInterface
from hardware_interfaces.actuators.servo.webots_servo import WebotsServo
from hardware_interfaces.actuators.servo.elsiros_servo import ElsirosServo


class GeneralPositionController(PositionControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode, config, clock):
        super().__init__(name, config, clock)

        self.agent = agent

        if mode == 'webots':
            for servo_config in self._servos.items():
                self._add_interface(WebotsServo(servo_config[0], agent, config, clock))
        elif mode == 'elsiros':
            for servo_config in self._servos.items():
                self._add_interface(ElsirosServo(servo_config[0], agent, config, clock))
        else:
            # ADDITION OF CUSTOM HRDWARE INTERFACE
            pass
