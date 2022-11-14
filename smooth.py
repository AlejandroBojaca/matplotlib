import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so
from scipy.interpolate import make_interp_spline


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
y = np.array([1, 1.23, 5.34, 15.4, 54.1, 146.42, 1, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])

print(z)

from scipy.interpolate import make_interp_spline

#define x as 200 equally spaced values between the min and max of original x 
xnew = np.linspace(x.min(), x.max(), 200) 

#define spline
spl = make_interp_spline(x, y, k=2)
y_smooth = spl(xnew)

#create smooth line chart 
plt.plot(xnew)
plt.show()