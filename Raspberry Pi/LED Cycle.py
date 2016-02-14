import RPi.GPIO as GPIO
import sys
import time

out_pins = [29, 31, 33, 35, 36, 37, 38, 40]

GPIO.setmode(GPIO.BOARD)
GPIO.setup( out_pins, GPIO.OUT, initial=GPIO.LOW)

for k in range(5):
    for i in range(8):
        asciiart=""
        for j in range(8):
            if i==j:
                GPIO.output(out_pins[j], True)
                asciiart+="* "
            else:
                GPIO.output(out_pins[j], False)
                asciiart+="- "
        print(asciiart[::-1])
        time.sleep(0.2)
 
GPIO.cleanup()


