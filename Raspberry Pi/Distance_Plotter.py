import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

speed_sound = 348 
echo = 7
trig = 11
dist = [0]*30
times = list(range(30))

def measure():
    GPIO.output(trig , True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start = time.time()
    while GPIO.input(echo) == 0:
        start = time.time()

    while GPIO.input(echo) == 1:
        stop = time.time()

    return round((stop-start)*speed_sound*100/2    , 4)


def animate(i):
    dist.pop(0)
    dist.append(measure())
    
    plt.cla()
    plt.title("Distance Plotter")
    plt.ylabel("Distance")
    plt.xlabel("Reading #")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.plot(dist, 'bo-', label='Distance cm')
    plt.legend(loc='upper left')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(echo, GPIO.IN)

fig = plt.figure()



time.sleep(2)
init_time = time.time()


try:
    ani = animation.FuncAnimation(fig, animate)
    plt.show()
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass
finally:  
    GPIO.cleanup()
    print ("GPIO Cleaned")



