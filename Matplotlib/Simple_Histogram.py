import math
import random 
import matplotlib.pyplot as plt

x = list(range(1,50))
age = [random.normalvariate(50,20) for i in x]
bins = list(range(0,100, 5))

plt.hist(age, bins, label='Ages Bar', color='#ffe600', rwidth=0.8, edgecolor='none')
plt.xlabel('Person No')
plt.ylabel('Age')
plt.title('Age Chart')
plt.legend()
plt.show()

