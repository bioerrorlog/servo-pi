import pytest
import time
from servo_gpio.servo import SnakeServo


class TestServo:
    @pytest.mark.parametrize('pin_num', [17, 18, 27])
    def test_set_get_servo_angle(self, monkeypatch, pin_num):
        monkeypatch.setenv('GPIOZERO_PIN_FACTORY', 'mock')
        monkeypatch.setenv('GPIOZERO_MOCK_PIN_CLASS', 'mockpwmpin')
        with SnakeServo(pin_num) as servo:
            servo.angle = 60
            assert servo.angle == 60
            servo.angle = 0
            assert servo.angle == 0

    def test_lead_another_servo(self, monkeypatch):
        monkeypatch.setenv('GPIOZERO_PIN_FACTORY', 'mock')
        monkeypatch.setenv('GPIOZERO_MOCK_PIN_CLASS', 'mockpwmpin')
        with SnakeServo(17) as leader_servo, SnakeServo(18) as follower_servo:
            leader_servo.wavelength = 0.2
            leader_servo.add_follower(follower_servo)

            # TODO: async process
            leader_servo.angle = 10
            follower_servo.angle = 0
            assert leader_servo.angle != follower_servo.angle

            leader_servo.start_wave(60)
            assert leader_servo.angle == follower_servo.angle