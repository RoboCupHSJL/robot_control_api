from controller_manager import ControllerManager
from controller import Robot
import time

def main():
    #rclpy.init()
    kondo_webots_cm = ControllerManager(type='Webots', robot=Robot())
    kondo_webots_cm._step()

    #while True:
    #    for controller in kondo_webots_cm.controllers:
    #        rclpy.spin_once(kondo_webots_cm.controllers[controller])
    #        kondo_webots_cm.controllers[controller].step()

    #rclpy.spin(kondo_webots_cm.controllers['imu'])
        
 
        
if __name__ == '__main__':
    main()