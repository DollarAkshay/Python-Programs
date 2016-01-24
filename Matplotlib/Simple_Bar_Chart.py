import math
import random 
import matplotlib.pyplot as plt

x = list(range(1,50))
y1 = [math.sin(i/5)*10 for i in x]
y2 = [math.cos(i/5)*10 for i in x]
y3 = [random.randrange(1, 100, 1) for i in x]

plt.bar(x, y3, label='Ages Bar', color='#ffe600')
plt.xlabel('Person No')
plt.ylabel('Age')
plt.title('Age Chart')
plt.legend()
plt.show()

