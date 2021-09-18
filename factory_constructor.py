from controllers.camera_controllers.factory_camera_controller \
    import GeneralCameraController
from controllers.imu_controllers.factory_imu_controller \
    import GeneralImuController
from controllers.servo_controllers.factory_position_controller \
    import GeneralPositionController

from clock_interface import ClockInterface
from config_parser import ConfigParser

class FactoryConstructor:
    def __init__(self, control_config, mode):
        self.controllers = {}

        self.agent = None

        if mode == 'webots':
            from controller import Robot
            self.agent = Robot()
        elif mode == 'elsiros':
            from elsiros_communicator import ElsirosCommunicator
            self.agent = ElsirosCommunicator()
            self.agent.enable()
        elif mode == 'test':
            self.agent = None
        else:
            # IMPORT AND ASSIGNMENT OF THE CUSTOM AGENT 
            pass

        clock = ClockInterface(mode, self.agent)
        config_p = ConfigParser(control_config)
        print('============================================')
        print(config_p.imu_class)
        print(config_p.servo_class)
        print(config_p.camera_class)


        self.controllers['imu'] = GeneralImuController('imu_controller', 
                                                       self.agent,
                                                       mode,
                                                       config_p.imu_class,
                                                       control_config,
                                                       clock)
        self.controllers['servos'] = GeneralPositionController('servo_controller', 
                                                               self.agent,
                                                               mode,
                                                               config_p.servo_class, 
                                                               control_config,
                                                               clock)
        self.controllers['camera'] = GeneralCameraController('camera_controller', 
                                                             self.agent, 
                                                             mode,
                                                             config_p.camera_class,
                                                             control_config,
                                                             clock)
            
        


