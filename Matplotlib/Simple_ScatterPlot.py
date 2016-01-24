import math
import random 
import matplotlib.pyplot as plt

x = list(range(1,20))
y = [random.normalvariate(50,0.001)*2 for i in x]

plt.scatter(x, y, label='Normal Dist', color='#ffe600', marker='h', s=500)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('BELL PLOT')
plt.legend()
plt.show()

