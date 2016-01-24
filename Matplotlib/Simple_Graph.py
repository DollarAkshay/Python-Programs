import math
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

x = list(range(1,1001))
y1 = [math.log(i,2) for i in x]
y2 = [math.log(i,3) for i in x]

plt.plot(x, y1, label='Log 2')
style.use('ggplot')
plt.plot(x, y2, label='Log 3')
plt.xlabel('x-axis')
plt.ylabel('Log to base e')
plt.title('Awesome Graph')
plt.legend()
plt.show()

