import numpy as np
import pandas as pd
import json

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so
from scipy.interpolate import make_interp_spline

info = {
  "chartType": "dark-profit-chart",
  "chartData": {
    "profits": [0, 1.23, 5.34, 15.4, 54.1, 146.42],
    "timestamps": [0, 1, 2, 3, 4, 5,],
    "userId": "794ee75b-30e8-4941-be45-1f397775985d"
  }
}

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
y = np.array([1, 1.23, 5.34, 15.4, 54.1, 146.42, 1, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])
extra_points = 200

#move y axis
# f = plt.figure()
# ax = f.add_subplot()
# ax.yaxis.tick_right()

#define x as 200 equally spaced values between the min and max of original x 
xnew = np.linspace(x.min(), x.max(), extra_points) 

#define spline
spl = make_interp_spline(x, y, k=2)
y_smooth = spl(xnew)
zero = [y_smooth.min() - 1] * y_smooth.size 

#create smooth line chart 
plot_info = pd.DataFrame({"timestamps": xnew, "profits": y_smooth})
# y_smooth = spl(xnew)

#resize
plt.figure(figsize=(13, 6))
plt.margins(y=0.1)
plt.subplots_adjust(top=0.6, bottom=0.2)

#delete axis
sns.despine(left=True, bottom=True, top=True, right=True)

#shade
plt.fill_between(
        x= xnew, 
        y1= y_smooth, 
        y2= zero,
        where= (-1 < xnew)&(xnew < 15),
        color= "b",
        alpha= 0.2)
#add texts
plt.text(0, 200, "Profit ALL\n256%", fontsize='large')
plt.text(2, 200, "MaxDD\n16%", fontsize='large')
plt.text(0, 300, "Username", fontsize='xx-large')


#ploting
plt.plot(xnew , y_smooth)
plt.savefig('test.svg')
# plt.show()

# info = json.loads(json.dumps(info))
# plotingInfo = pd.DataFrame(info["chartData"])

