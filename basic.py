import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt


T = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
power = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])

plt.plot(T , power)
plt.show()