import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from drawnow import *
import time

speed_sound = 348 
echo = 7
trig = 11
dist = [0]*30
times = list(range(20))

def measure():
    GPIO.output(trig , True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start = time.time()
    while GPIO.input(echo) == 0:
        start = time.time()

    while GPIO.input(echo) == 1:
        stop = time.time()

    return round((stop-start)*speed_sound*100/2 , 4)

def makefig():
    plt.title("Distance Graph")
    plt.ylabel("Distance")
    plt.xlabel("Reading")
    plt.ylim(0, 70)
    plt.grid(True)
    plt.plot(dist, 'ro-', label="Distance cm")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(echo, GPIO.IN)
plt.ion()

time.sleep(1)

try:
    while True:
        dist.pop(0)
        dist.append(measure())
        drawnow(makefig)
        plt.pause(0.001)
        
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass
finally:  
    GPIO.cleanup()
    print ("GPIO Cleaned")



