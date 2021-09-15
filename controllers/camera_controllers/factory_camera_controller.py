# TODO: add docs
from .camera_controller_interface import CameraControllerInterface
from hardware_interfaces.sensors.camera.webots_camera import WebotsCamera
from hardware_interfaces.sensors.camera.elsiros_camera import ElsirosCamera

class GeneralCameraController(CameraControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode, config, clock):
        super().__init__(name, clock)

        self.agent = agent

        if mode == 'webots':
            self._add_interface(WebotsCamera(name='camera', agent=agent, config=config, clock=clock))
        elif mode == 'elsiros':
            self._add_interface(ElsirosCamera(name='camera', agent=agent, config=config, clock=clock))
        else:
            # ADDITION OF CUSTOM HARDWARE INTERFACE
            pass
