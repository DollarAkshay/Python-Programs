
import RPi.GPIO as GPIO
import time

echo = 3
trig = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, 0)

time.sleep(0.1)

print "Starting Measurment..."

GPIO.output(trig , 1)
time.sleep(0.00001)
GPIO.output(trig, 0)

while GPIO.input(echo) == 0:
    pass

start = time.time()

while GPIO.input(echo) == 1:
    pass

stop = time.time()

print (stop-start)*17000

GPIO.cleanup()




