import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns

T = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
power = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])
f = plt.figure()
ax = f.add_subplot(111)
ax.yaxis.tick_right()

#delete axis
sns.despine(left=True, bottom=True, top=True, right=True)
ax.tick_params(length=0, colors='k')

#add custom labels to ticks
# labels = [item.get_text() for item in ax.get_xticklabels()]
# labels[1] = 'Testing'

ax.yaxis.set_major_formatter('%{x:1.0f}')

# ax.set_xticklabels(labels)

plt.plot(T , power)
plt.show()