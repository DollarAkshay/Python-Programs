import smbus
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
address = 0x68

ac_x = [0]*10
ac_y = [0]*10
ac_z = [0]*10
times = list(range(30))

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    val = (read_byte(adr)<<8) + read_byte(adr+1)
    if val >= 2**15:
        val -= 2**16
    return val


def animate(i):
    
    ac_x.pop(0)
    ac_x.append(read_word(0x3B)/16384)

    ac_y.pop(0)
    ac_y.append(read_word(0x3D)/16384)

    ac_z.pop(0)
    ac_z.append(read_word(0x3F)/16384)
    
    plt.cla()
    plt.title("Distance Plotter")
    plt.ylabel("Value")
    plt.xlabel("Reading #")
    plt.ylim(-3, 3)
    plt.grid(True)
    plt.plot(ac_x, 'ro-', label='X-Axis')
    plt.plot(ac_y, 'go-', label='Y-Axis')
    plt.plot(ac_z, 'bo-', label='Z-Axis')
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



