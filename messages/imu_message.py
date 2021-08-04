# TODO: add docs
import logging
import math


def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)

    return roll_x, pitch_y, yaw_z  # in radians


class IMUMessage:
    """[summary]

    Raises:
        Exception: [description]

    Returns:
        [type]: [description]
    """
    class Orientation:
        """[summary]
        """
        def __init__(self, *args):
            assert len(args) == 3 and \
                all([isinstance(args[i], float) for i in range(len(args))])
            self.pitch = None
            self.roll = None
            self.yaw = None
            if len(args) == 3:
                self.pitch = args[0]
                self.roll = args[1]
                self.yaw = args[2]

    def __init__(self):
        self.__timestamp = None
        self.__orientation = None

    @property
    def timestamp(self):
        """[summary]
        """
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        try:
            assert isinstance(timestamp, int, float)
            self.__timestamp = timestamp
        except AssertionError as assertion:
            logging.error("timestamp value must be an int or float")
            raise Exception("timestamp value must be an int or float") \
                from assertion

    @property
    def orientation(self):
        """[summary]
        """
        return self.__orientation

    @orientation.setter
    def orientation(self, *args):
        """[summary]

        Args:
            orientation ([type]): [description]
        """
        if isinstance(args[0], self.Orientation) and len(args) == 1:
            self.__orientation = args[0]
        elif len(args) == 3 and all([isinstance(args[i], float) for i in range(len(args))]):
            self.__orientation = self.Orientation(*args)
        elif isinstance(args[0], list, tuple) and len(args) == 1:
            self.__orientation = self.Orientation(*args[0])
