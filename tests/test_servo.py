import pytest
from servo_gpio.servo import Servo


@pytest.mark.parametrize('pin_num', [17, 18, 27])
def test_get_servo_angle(monkeypatch, pin_num):
    monkeypatch.setenv('GPIOZERO_PIN_FACTORY', 'mock')
    monkeypatch.setenv('GPIOZERO_MOCK_PIN_CLASS', 'mockpwmpin')
    servo = Servo(pin_num)
    servo.set_angle(60)
    assert servo.get_angle() == 60