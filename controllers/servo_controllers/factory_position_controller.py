# TODO: add docs
from .position_controller_interface import PositionControllerInterface


class GeneralPositionController(PositionControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode, hw_class, config, clock):
        super().__init__(name, config, clock)

        self.agent = agent

        if mode == 'webots':
            for servo_config in self._servos.items():
                self._add_interface(hw_class(servo_config[0], agent, config, clock))
        elif mode == 'elsiros':
            for servo_config in self._servos.items():
                self._add_interface(hw_class(servo_config[0], agent, config, clock))
        else:
            for servo_config in self._servos.items():
                try:
                    self._add_interface(hw_class(servo_config[0], agent, config, clock))
                except:
                    raise Exception('Incorrect Servo class')
