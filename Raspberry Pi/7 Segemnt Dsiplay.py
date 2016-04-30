import RPi.GPIO as GPIO
import time

segment = [33, 31, 38, 36, 32, 35, 37, 40]

# Link to Video : https://www.youtube.com/watch?v=l2irGcM5Wf4

GPIO.setmode(GPIO.BOARD)
GPIO.setup(segment, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        for pin in segment:
            GPIO.output(pin, 1)
            time.sleep(0.25)
        time.sleep(1)
        for pin in segment:
            GPIO.output(pin, 0)
            time.sleep(0.25)
        for pin in segment:
            GPIO.output(pin, 1)
            time.sleep(0.25)
            GPIO.output(pin, 0)
    
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass
finally :
    GPIO.cleanup()
