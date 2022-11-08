import numpy as np
import pandas as pd
import json

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
from scipy.interpolate import make_interp_spline, BSpline

plot_size = 10

time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
profits = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])


# 300 represents number of points to make between time.min and time.max
xnew = np.linspace(time.min(), time.max(), plot_size) 


spl = make_interp_spline(time, profits, k=3)  # type: BSpline
profits_smooth = spl(xnew)

min_profit = profits_smooth.min() - 1
zero = np.array([min_profit]*plot_size)


plotingInfo = pd.DataFrame({"timestamps": xnew, "profits": profits_smooth})

# plt.plot(xnew, profits_smooth)

sns.relplot(
    data=plotingInfo, 
    kind="line",
    x="timestamps",
    y="profits",
)

plt.fill_between(
        x= xnew, 
        y1= profits_smooth, 
        y2= zero,
        where= (-1 < xnew)&(xnew < 15),
        color= "b",
        alpha= 0.2)

sns.despine(left=True, bottom=True)

# plt.fill_between

# sns.kdeplot(xnew, color="orange", fill=True)

plt.show()
# plt.savefig('test.svg')