from time import time

class ClockInterface:
    def getTime(self):
        pass

    def __init__(self, mode, agent):
        if mode == 'webots':
            def tmp_func():
                return agent.getTime()
            self.getTime = tmp_func

        elif mode == 'elsiros':
            def tmp_func():
                return agent.get_time()
            self.getTime = tmp_func
            
        else:
            def tmp_func():
                return time()
            self.getTime = tmp_func
