# TODO: add docs
from .camera_controller_interface import CameraControllerInterface
from hardware_interfaces.sensors.camera.webots_camera import WebotsCamera


class WebotsCameraController(CameraControllerInterface):
    """[summary]

    Args:
        CameraControllerInterface ([type]): [description]
    """
    def __init__(self, name, agent):
        super().__init__(name)

        self.agent = agent

        self._add_interface(WebotsCamera(name='camera', agent=agent))
