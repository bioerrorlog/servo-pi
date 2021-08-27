import math
import time
from gpiozero import AngularServo
from servo import SnakeServo

def main():
    # servo_17 = SnakeServo(17, wavelength=0.2)
    # servo_18 = SnakeServo(18, wavelength=0.2)
    # servo_27 = SnakeServo(27, wavelength=0.2)
    servo_17 = AngularServo(17)
    servo_18 = AngularServo(18)
    servo_27 = AngularServo(27)

    # servo_17.add_follower(servo_18)
    # servo_18.add_follower(servo_27)

    t = 0
    max_angle = 90
    gap_angle = 60
    while True:
        servo_17.angle = math.sin(math.radians(t % 360)) * max_angle
        servo_18.angle = math.sin(math.radians((t % 360) + gap_angle)) * max_angle
        servo_27.angle = math.sin(math.radians((t % 360) + (gap_angle * 2))) * max_angle

        t += 2
        time.sleep(0.01)
    
if __name__ == '__main__':
    main()