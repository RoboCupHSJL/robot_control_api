# TODO: add docs
from controllers import ControllerInterface


class CameraControllerInterface(ControllerInterface):
    """[summary]

    Args:
        ControllerInterface ([type]): [description]
    """
    def step(self):
        """[summary]
        """
        for camera in self.hardware_interfaces.values():
            camera.read()
