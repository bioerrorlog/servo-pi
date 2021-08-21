from gpiozero import AngularServo
from servo import SnakeServo

def main():
    servo_17 = SnakeServo(17, wavelength=0.2)
    servo_18 = SnakeServo(18, wavelength=0.2)
    servo_27 = SnakeServo(27, wavelength=0.2)

    servo_17.add_follower(servo_18)
    servo_18.add_follower(servo_27)

    while True:
        servo_17.start_wave(60)
        servo_17.start_wave(-60)

    
if __name__ == '__main__':
    main()