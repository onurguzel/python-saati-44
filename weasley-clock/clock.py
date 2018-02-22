import RPi.GPIO as GPIO
import pico
from pico import PicoApp
from zones import zones

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(2.5)


def set_angle(angle):
    global pwm
    duty = float(angle) / 20.0 + 2.5
    pwm.ChangeDutyCycle(duty)


@pico.expose()
def ping(zone):
    set_angle(zones[zone])

app = PicoApp()
app.register_module(__name__)
