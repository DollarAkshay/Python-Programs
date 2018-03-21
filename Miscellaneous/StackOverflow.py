import math
import random
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

pre_lo = [-0.493]
post_lo = [0.145]
lo_label = ['lo']

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, color='black')
labels = ['Label 1', 'Label B', 'Label 03', 'Label D', 'Label E']

for i, txt in enumerate(labels):
    ax1.annotate(labels[i], (x[i], y[i]))


plt.show()
