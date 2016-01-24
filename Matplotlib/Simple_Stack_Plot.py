import math
import random 
import matplotlib.pyplot as plt

x = list(range(0,5))
s1 = [random.normalvariate(5,1) for i in x]
s2 = [random.normalvariate(7,2) for i in x]
s3 = [random.normalvariate(2,1) for i in x]
s4 = [24-s1[i]-s2[i]-s3[i] for i in x]

print(min(s1),min(s2),min(s3),min(s4))
plt.stackplot(x, s1, s2, s3, s4, colors=['r','yellow','green','b'], edgecolor='none')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Stack PLOT')
plt.legend()
plt.show()

