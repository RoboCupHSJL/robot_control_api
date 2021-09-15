import queue
from messages.servo_cmd_message import ServoCmdMessage

class Interactor(dict):
    def __init__(self):
        super().__init__()
        #self.__pos_queue = queue.Queue()
        self.__curr_msg = None

    @property
    def topic_list(self):
        return list(self.keys())

    def push_message(self, channel, msg):
        if channel == 'servo_cmd':
            assert isinstance(msg, ServoCmdMessage), \
                "Only objects of type ServoCmdMessage can be pushed into servo_cmd channel"
            self.__curr_msg = msg
        else:
            raise NotImplementedError

    def get_message(self, channel):
        if channel == 'servo_cmd':
            return self.__curr_msg
        elif channel is self.__curr_msg.frame:
            return self.__curr_msg.frame[channel]
        else:
            raise Exception('trying to read from non existent interactor channel')
            
    @property
    def cmd_empty(self):
        return self.__curr_msg is None