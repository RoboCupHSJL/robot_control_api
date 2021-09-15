# TODO: add docs
import time
from .clock_interface import ClockInterface


class RealClock(ClockInterface):
    """[summary]

    :param ClockInterface: [description]
    :type ClockInterface: [type]
    """
    def now(self):
        return time.time()
