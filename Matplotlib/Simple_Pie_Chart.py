import math
import random 
import matplotlib.pyplot as plt

x = list(range(1,6))
slices = [i*i for i in x]

plt.pie(slices, labels=x, startangle=90, shadow=True, wedgeprops={'linewidth':0}, explode=(0,0,0.2,0,0))
plt.title('Pie Chart')
plt.show()

