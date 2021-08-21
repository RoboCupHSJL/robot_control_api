# TODO: add docs
from .camera_controller_interface import CameraControllerInterface
from hardware_interfaces.sensors.camera.webots_camera import WebotsCamera
from hardware_interfaces.sensors.camera.elsiros_camera import ElsirosCamera

class GeneralCameraController(CameraControllerInterface):
    """[summary]

    Args:
        PositionControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent, mode):
        super().__init__(name)

        self.agent = agent

        if mode == 'webots':
            self._add_interface(WebotsCamera(name='camera', agent=agent))
        elif mode == 'elsiros':
            self._add_interface(ElsirosCamera(name='camera', agent=agent))
        else:
            # ADDITION OF CUSTOM HARDWARE INTERFACE
            pass
