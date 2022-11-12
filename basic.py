import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt


T = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
power = np.array([0, 100.23, 500.34, 1500.4, 5400.1, 14600.42, 0, 100.23, 500.34, 1500.4, 5400.1])
number_x = T.size

ax = plt.axes()
# plt.annotate('Something', xy=(0.5, 0.5), xycoords='axes fraction')
for x in range(number_x):
    plt.text(x=x/number_x, y=-0.1, s='TEST', transform=ax.transAxes)

plt.plot(T , power)
plt.show()