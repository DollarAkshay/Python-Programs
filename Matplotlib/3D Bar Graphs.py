import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


style.use('fivethirtyeight')
fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x = list(range(1,20))
y = [math.log(i, 2) for i in x]
z = np.ones(len(x))
dx = np.ones(len(x))
dy = np.ones(len(x))
dz = [math.sin(i/10) for i in x]
ax1.bar3d(x,y,z, dx, dy, dz)


ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')

plt.show()





