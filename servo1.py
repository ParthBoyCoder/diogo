import RPi.GPIO as gpio
import time

pin=12
duty=0

gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT)

pwm=gpio.PWM(12, 50)
pwm.start(0)

def set_angle(angle):
    duty=2+(angle/18)
    gpio.output(12,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.4)
    gpio.output(12,gpio.LOW)
    pwm.ChangeDutyCycle(0)

a=int(input("enter angle: "))
set_angle(a)