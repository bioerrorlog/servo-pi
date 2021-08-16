from servo_gpio.servo import Servo
import os


def test_get_servo_angle(monkeypatch):
    monkeypatch.setenv('GPIOZERO_PIN_FACTORY', 'mock')
    monkeypatch.setenv('GPIOZERO_MOCK_PIN_CLASS', 'mockpwmpin')
    servo = Servo(18)
    servo.set_angle(60)
    assert servo.get_angle() == 60