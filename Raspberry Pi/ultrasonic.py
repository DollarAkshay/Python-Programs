import RPi.GPIO as GPIO
import time

speed_sound = 348 

echo = 7
trig = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(echo, GPIO.IN)

time.sleep(2)

print "Starting Measurment..."

GPIO.output(trig , True)
time.sleep(0.00001)
GPIO.output(trig, False)

start = time.time()
while GPIO.input(echo) == 0:
    start = time.time()

while GPIO.input(echo) == 1:
    stop = time.time()

dist = (stop-start)*speed_sound*100/2
print "Distance : %.4f" % dist

GPIO.cleanup()



