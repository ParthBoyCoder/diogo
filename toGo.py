import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

gpio.output(18, gpio.HIGH)