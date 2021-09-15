import logging
from .message import Message

class ServoCmdMessage(Message):
    """[summary]

    Raises:
        Exception: [description]

    Returns:
        [type]: [description]
    """
    def __init__(self):
        super().__init__()
        self.__frame = None

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, *args):
        """[summary]

        Args:
            frame (dict):dict of servo names (str) and positions (float)
        """
        if isinstance(args[0], dict):
            for i, v in args[0].items():
                assert isinstance(i, str), "when creating Servo Command servo names must be string"
                assert isinstance(v, (float, int)), "When creating Servo Command Message servo position values must be either float or int"
            self.__frame = args[0]
        else:
            pass