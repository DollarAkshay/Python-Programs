import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x = list(range(1,1000))
y = [math.log(i, 2) for i in x]
z = [math.sin(i/10) for i in x]

ax1.plot_wireframe(x,y,z)


ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')

plt.show()





