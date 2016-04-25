import smbus
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
address = 0x68

gy_x = [0]*10
gy_y = [0]*10
gy_z = [0]*10
times = list(range(30))

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    val = (read_byte(adr)<<8) + read_byte(adr+1)
    if val >= 2**15:
        val -= 2**16
    return val


def animate(i):
    
    gy_x.pop(0)
    gy_x.append(gy_x[-1]+read_word(0x43)/131)

    gy_y.pop(0)
    gy_y.append(gy_y[-1]+read_word(0x45)/131)

    gy_z.pop(0)
    gy_z.append(gy_z[-1]+read_word(0x47)/131)
    
    plt.cla()
    plt.title("Distance Plotter")
    plt.ylabel("Value")
    plt.xlabel("Reading #")
    plt.ylim(-200, 200)
    plt.grid(True)
    plt.plot(gy_x, 'ro-', label='X-Axis')
    plt.plot(gy_y, 'go-', label='Y-Axis')
    plt.plot(gy_z, 'bo-', label='Z-Axis')
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



