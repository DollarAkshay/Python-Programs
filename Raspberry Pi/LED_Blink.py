import RPi.GPIO as GPIO
import time

inpin = 11
outpin = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(inpin , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(outpin , GPIO.OUT)

for i in range(1000):
    
    if GPIO.input(inpin)==True:
        print("Pressed")
        GPIO.output(outpin, True)
    else:
        print("Not Pressed")
        GPIO.output(outpin, False)
        
    time.sleep(0.1)

GPIO.cleanup()
