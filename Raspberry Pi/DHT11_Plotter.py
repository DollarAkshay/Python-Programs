import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

speed_sound = 348 
echo = 7
trig = 11
temp = [0]*30
hum = [0]*30
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
    
    h,t = dht.read_retry(dht.DHT11, 4)
    temp.pop(0)
    temp.append(t)
    hum.pop(0)
    hum.append(h)
    
    plt.cla()
    plt.title("Distance Plotter")
    plt.ylabel("Distance")
    plt.xlabel("Reading #")
    plt.ylim(0, 80)
    plt.grid(True)
    plt.plot(temp, 'bo-', label='Temp C')
    plt.plot(hum, 'ro-', label='Humidity %')
    plt.legend(loc='best')
    

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



