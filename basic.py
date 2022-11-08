import numpy as np
import pandas as pd
import json

import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline


T = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
power = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])


# 300 represents number of points to make between T.min and T.max

plt.plot(T , power)
plt.show()


info = {
  "chartType": "dark-profit-chart",
  "chartData": {
    "profits": [0, 1.23, 5.34, 15.4, 54.1, 146.42],
    "timestamps": [0, 1, 2, 3, 4, 5,],
    "userId": "794ee75b-30e8-4941-be45-1f397775985d"
  }
}