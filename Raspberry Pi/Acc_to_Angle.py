import smbus
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import math

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
address = 0x68

ang_x = [0]*10
ang_y = [0]*10
ang_z = [0]*10
times = list(range(30))

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    val = (read_byte(adr)<<8) + read_byte(adr+1)
    if val >= 2**15:
        val -= 2**16
    return val


def animate(i):

    ax = read_word(0x3B)/16384
    ay = read_word(0x3D)/16384
    az = read_word(0x3F)/16384

    tx = math.degrees( math.atan2(ax, math.sqrt(ay*ay+az*az)))
    ty = math.degrees( math.atan2(ay, math.sqrt(ax*ax+az*az)))
    tz = math.degrees( math.atan2(math.sqrt(ax*ax+ay*ay), az))
    
    ang_x.pop(0)
    ang_x.append(tx)

    ang_y.pop(0)
    ang_y.append(ty)

    ang_z.pop(0)
    ang_z.append(tz)
    
    plt.cla()
    plt.title("Distance Plotter")
    plt.ylabel("Angle")
    plt.xlabel("Reading #")
    plt.ylim(-200, 200)
    plt.yticks(np.arange(-180, 180, 45))
    plt.grid(True)
    plt.plot(ang_x, 'ro-', label='X-Axis')
    plt.plot(ang_y, 'go-', label='Y-Axis')
    plt.plot(ang_z, 'bo-', label='Z-Axis')
    plt.legend(loc='upper left')

    
bus = smbus.SMBus(1)
bus.write_byte_data(address, power_mgmt_1, 0)
      

fig = plt.figure()



try:
    ani = animation.FuncAnimation(fig, animate)
    plt.show()
except KeyboardInterrupt:
    print ("Forced Key Exit")
except:
    pass



