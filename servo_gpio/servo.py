import time
from gpiozero import AngularServo


class SnakeServo(AngularServo):
    def __init__(self, pin=None, *, initial_angle=0.0, min_angle=-90,
                 max_angle=90, min_pulse_width=1/1000, max_pulse_width=2/1000,
                 frame_width=20/1000, pin_factory=None):
        self._followers = []
        super().__init__(pin, initial_angle=initial_angle,
                         min_angle=min_angle, max_angle=max_angle,
                         min_pulse_width=min_pulse_width,
                         max_pulse_width=max_pulse_width,
                         frame_width=frame_width, pin_factory=pin_factory)

    def add_follower(self, follower):
        self._followers.append(follower)

    def start_wave(self, angle, wavelength=0.2):
        self.angle = angle
        time.sleep(wavelength)
        for servo in self._followers:
            servo.start_wave(angle, wavelength)