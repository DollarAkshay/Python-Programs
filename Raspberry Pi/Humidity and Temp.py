import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

def bin2dec(string_num):
    return str(int(string_num, 2))

data = []

pini = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pini,GPIO.OUT)
GPIO.output(pini,GPIO.HIGH)
time.sleep(0.025)
GPIO.output(pini,GPIO.LOW)
time.sleep(0.02)
GPIO.setup(pini, GPIO.IN, pull_up_down=GPIO.PUD_UP)


for i in range(0,1700):
    data.append(GPIO.input(pini))

data2 = []

fig = plt.figure()
try:
    plt.plot(data)
    plt.ylim(-0.5, 1.5)
    plt.show()
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass
finally:  
    GPIO.cleanup()
    print ("GPIO Cleaned")

