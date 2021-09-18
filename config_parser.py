import logging
import importlib

class ConfigParser:
    def __init__(self, config):
        if config.get("hw_interface") is None:
            raise Exception('Hardware Interface classes not specified in the configuration file. \
                             Please use the key word "hw_interface"')
        self.__config = config
        self.__servo_class = None
        self.__imu_class = None
        self.__camera_class = None

        self.parse_hw(config.get('hw_interface'))

    def parse_hw(self, hw_config):
        if not hw_config.get('servo'):
            raise Exception('Servo interface not specified in the configuration file. \
                             Please use the key word "servo"')

        if not hw_config.get('imu'):
            raise Exception('Imu interface not specified in the configuration file. \
                             Please use the key word "imu"')

        if not hw_config.get('camera'):
            raise Exception('Camera interface not specified in the configuration file. \
                             Please use the key word "camera"')
            
        if hw_config.get('servo') == 'WebotsServo':
            from hardware_interfaces.actuators.servo.webots_servo import WebotsServo
            self.__servo_class = WebotsServo

        elif hw_config.get('servo') == 'ElsirosServo':
            from hardware_interfaces.actuators.servo.elsiros_servo import ElsirosServo
            self.__servo_class = ElsirosServo        

        else:
            path = hw_config.get('servo').strip('/')
            mod_name = '.'.join(path.split('/')[:-1])
            class_name = path.split('/')[-1]
            try:
                mod = importlib.import_module(mod_name)
            except:
                raise Exception('Incorrect custom Servo Class module path')
            try:
                class_ = getattr(mod, class_name)
            except:
                raise Exception('Incorrect custom Servo Class name')
            self.__servo_class = class_


        if hw_config.get('imu') == 'WebotsIMU':
            from hardware_interfaces.sensors.imu.webots_imu import WebotsIMU
            self.__imu_class = WebotsIMU

        elif hw_config.get('imu') == 'ElsirosIMU':
            from hardware_interfaces.sensors.imu.elsiros_imu import ElsirosIMU
            self.__imu_class = ElsirosIMU

        else:
            path = hw_config.get('imu').strip('/')
            mod_name = '.'.join(path.split('/')[:-1])
            class_name = path.split('/')[-1]
            try:
                mod = importlib.import_module(mod_name)
            except:
                raise Exception('Incorrect custom IMU Class module path')
            try:
                class_ = getattr(mod, class_name)
            except:
                raise Exception('Incorrect custom IMU Class name')
            self.__imu_class = class_


        if hw_config.get('camera') == 'WebotsCamera':
            from hardware_interfaces.sensors.camera.webots_camera import WebotsCamera
            self.__camera_class = WebotsCamera

        elif hw_config.get('camera') == 'ElsirosCamera':
            from hardware_interfaces.sensors.camera.elsiros_camera import ElsirosCamera
            self.__camera_class = ElsirosCamera

        else:
            path = hw_config.get('camera').strip('/')
            mod_name = '.'.join(path.split('/')[:-1])
            class_name = path.split('/')[-1]
            try:
                print(mod_name)
                print(class_name)
                mod = importlib.import_module(mod_name)
            except:
                raise Exception('Incorrect custom Camera Class module path')
            try:
                class_ = getattr(mod, class_name)
                print(class_)
            except:
                raise Exception('Incorrect custom Camera Class name')
            self.__camera_class = class_

    @property
    def servo_class(self):
        return self.__servo_class

    @property
    def imu_class(self):
        return self.__imu_class

    @property
    def camera_class(self):
        return self.__camera_class

        