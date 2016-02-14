import RPi.GPIO as GPIO
import time

pin = 40
led_on = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

for i in range(10,0,-1):
    GPIO.output(pin, led_on)
    time.sleep(i/5)
    led_on = not led_on

GPIO.cleanup()
