class HWInterface:
    def __init__(self, name):
        self._name = name
        self._status = 'disabled'

    def get_param(self, param_name):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def get_name(self):
        return self._name

    def get_status(self):
        return self._status