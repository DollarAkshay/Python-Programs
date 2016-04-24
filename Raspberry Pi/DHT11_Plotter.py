import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

temp = [0]*30
hum = [0]*30


def animate(i):
    
    h,t = dht.read_retry(dht.DHT11, 4)
    temp.pop(0)
    hum.pop(0)
    temp.append(t)
    hum.append(h)
    
    plt.cla()
    plt.title("Distance Plotter")
    plt.xlabel("Reading #")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.plot(temp, 'ro-', label='Temp C')
    plt.plot(hum, 'bo-', label='Humidity %')
    plt.legend(loc='best')
    

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)

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



