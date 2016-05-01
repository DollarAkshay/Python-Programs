import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

ip1 = 11
ip2 = 13

pin1 = [0]*30
pin2 = [0]*30

def animate(i):
    pin1.pop(0)
    pin1.append(GPIO.input(ip1))

    pin2.pop(0)
    pin2.append(GPIO.input(ip2))
    
    plt.cla()
    plt.title("Distance Plotter")
    plt.ylabel("Distance")
    plt.xlabel("Reading #")
    plt.ylim(-1, 2)
    plt.grid(True)
    plt.plot(pin1, 'bo-', label='I/P 1')
    plt.plot(pin2, 'ro-', label='I/P 2')
    plt.legend(loc='best')


GPIO.setmode(GPIO.BOARD)
GPIO.setup(ip1, GPIO.IN)
GPIO.setup(ip2, GPIO.IN)
fig = plt.figure()

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
