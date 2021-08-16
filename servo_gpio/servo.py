from gpiozero import AngularServo


class Servo:
    def __init__(self, gpio_num):
        self.servo = AngularServo(gpio_num, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

    def set_angle(self, angle):
        self.servo.angle = int(angle)

    def get_angle(self):
        return self.servo.angle