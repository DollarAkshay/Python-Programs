import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pins = [3, 5, 7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40]
GPIO.setup(pins , GPIO.OUT)
print "Cleaning Up..."
GPIO.cleanup()
