import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
plt1 = fig.add_subplot(1,1,1)
lgbase = 2

def animate(k):
    global lgbase
    x = list(range(1,lgbase))
    y = [math.log(i,2) for i in x]
    plt1.plot(x,y)
    lgbase+=1
    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
