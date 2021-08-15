from gpiozero import AngularServo
from guizero import App, Slider

servo_18 = AngularServo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
servo_17 = AngularServo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
servo_27 = AngularServo(27, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def slider_changed_18(angle):
    servo_18.angle = int(angle)
    
def slider_changed_17(angle):
    servo_17.angle = int(angle)
    
def slider_changed_27(angle):
    servo_27.angle = int(angle)
    
app_18 = App(title='Servo Angle 18', width=500, height=150)
app_17 = App(title='Servo Angle 17', width=500, height=150)
app_27 = App(title='Servo Angle 17', width=500, height=150)
slider_18 = Slider(app_18, start=-90, end=90, command=slider_changed_18, width='fill', height=50)
slider_17 = Slider(app_17, start=-90, end=90, command=slider_changed_17, width='fill', height=50)
slider_27 = Slider(app_27, start=-90, end=90, command=slider_changed_27, width='fill', height=50)
slider_18.text_size = 30
slider_17.text_size = 30
slider_27.text_size = 30
app_18.display()
app_17.display()
app_27.display()