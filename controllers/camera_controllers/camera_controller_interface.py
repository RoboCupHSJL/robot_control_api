# TODO: add docs
from controllers import ControllerInterface
from global_ import interactor


class CameraControllerInterface(ControllerInterface):
    """[summary]

    Args:
        ControllerInterface ([type]): [description]
    """
    def step(self):
        """[summary]
        """
        for camera in self.hardware_interfaces.values():
            interactor[camera.name] = camera.read()
