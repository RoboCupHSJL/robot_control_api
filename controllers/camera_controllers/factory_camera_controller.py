# TODO: add docs
from .camera_controller_interface import CameraControllerInterface

class GeneralCameraController(CameraControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode, hw_class, config, clock):
        super().__init__(name, clock)

        self.agent = agent

        if mode == 'webots':
            self._add_interface(hw_class(name='camera', agent=agent, config=config, clock=clock))
        elif mode == 'elsiros':
            self._add_interface(hw_class(name='camera', agent=agent, config=config, clock=clock))
        else:
            try:
                print(hw_class)
                self._add_interface(hw_class(name='camera', agent=agent, config=config, clock=clock))
            except:
                raise Exception('Incorrect Camera class')
