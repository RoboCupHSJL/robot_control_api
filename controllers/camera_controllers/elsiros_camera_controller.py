# TODO: add docs
from .camera_controller_interface import CameraControllerInterface
from hardware_interfaces.sensors.camera.elsiros_camera import ElsirosCamera


class ElsirosCameraController(CameraControllerInterface):
    """[summary]

    Args:
        CameraControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent):
        super().__init__(name)

        self._add_interface(ElsirosCamera(name='camera', agent=agent))
