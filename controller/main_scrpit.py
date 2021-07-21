from controller_manager import ControllerManager
import rclpy

def main():
    rclpy.init()
    kondo_webots_cm = ControllerManager(type='Webots')
    while True:
        for controller in kondo_webots_cm.controllers:
            #rclpy.spin_once(kondo_webots_cm.controllers[controller])
            kondo_webots_cm.controllers[controller].step()

    #rclpy.spin(kondo_webots_cm.controllers['imu'])
        
 
        
if __name__ == '__main__':
    main()