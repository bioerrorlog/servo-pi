import pytest
from servo_gpio.servo import SnakeServo


class TestServo:
    @pytest.mark.parametrize('pin_num', [17, 18, 27])
    def test_set_get_servo_angle(self, monkeypatch, pin_num):
        monkeypatch.setenv('GPIOZERO_PIN_FACTORY', 'mock')
        monkeypatch.setenv('GPIOZERO_MOCK_PIN_CLASS', 'mockpwmpin')
        servo = SnakeServo(pin_num)
        servo.set_angle(60)
        assert servo.angle == 60

    # def test_lead_another_servo(self, monkeypatch):
    #     monkeypatch.setenv('GPIOZERO_PIN_FACTORY', 'mock')
    #     monkeypatch.setenv('GPIOZERO_MOCK_PIN_CLASS', 'mockpwmpin')
    #     leader_servo = SnakeServo(17)
    #     follower_servo = SnakeServo(18)
    #     leader_servo.set_follower(0)
    #     assert servo.get_angle() == 60