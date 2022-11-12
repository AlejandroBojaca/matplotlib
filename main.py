import numpy as np
import pandas as pd
import json

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data

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

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
y = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 50.34, 15.4, 10, 100])
size = x.size
extra_points = 150
background_color = 'white'

#font
plt.rcParams['font.family'] = 'roboto'

#create smooth line chart 
#define x as 200 equally spaced values between the min and max of original x 
xnew = np.linspace(x.min(), x.max(), extra_points)
#define spline
spl = make_interp_spline(x, y, k=2)
y_smooth = spl(xnew)
zero = [y_smooth.min() - 1] * y_smooth.size 
plot_info = pd.DataFrame({"timestamps": xnew, "profits": y_smooth})

#resize
#background color
px = 1/plt.rcParams['figure.dpi']
fig = plt.figure(figsize=(1024*px, 512*px), facecolor=background_color)
plt.subplots_adjust(top=0.63, bottom=0.23, left=0.05, right=0.89)

#images
binance_logo = plt.imread(get_sample_data('binance_logo.png'))
newax = fig.add_axes([0.14, 0.89, 0.05, 0.05])
newax.imshow(binance_logo)
newax.axis('off')
user_logo = plt.imread(get_sample_data('avatar.png'))
newax = fig.add_axes([0.79, 0.83, 0.05, 0.05])
newax.imshow(user_logo)
newax.axis('off')
qr_logo = plt.imread(get_sample_data('qr.png'))
newax = fig.add_axes([0.86, 0.83, 0.12, 0.12])
newax.imshow(qr_logo)
newax.axis('off')



#backgroundcolor
ax = plt.axes()
sns.despine(left=True, bottom=True, top=True, right=True)
ax.set_facecolor(background_color)
plt.tick_params(
    axis='both',          
    which='both',      
    bottom=False,
    left=False, 
    right=False,
    labelbottom=False,
    labelright=True,
    labelleft=False,
    pad=10,
    labelcolor=(0, 0, 0, 0.5),
    )
plt.margins(x=0)

#shade
plt.fill_between(
        x= xnew, 
        y1= y_smooth, 
        y2= zero,
        where= (-1 < xnew)&(xnew < 15),
        color= "#ED932E",
        alpha= 0.2
    )


#add texts

plt.text(0, 1.66, "Portfolio", fontsize='xx-large', fontweight=500, transform=ax.transAxes)
plt.text(0, 1.55, "TradeLink portfolio • tracking for 35 days since Jan 01, 2020", fontsize='small', color='#00000080', transform=ax.transAxes)

def generate_top_text(position, top_text, bottom_text): 
  plt.text(position, 1.25, top_text, fontsize='medium', color="#000000bf",  transform=ax.transAxes)
  plt.text(position, 1.1, bottom_text, fontsize='x-large', fontweight=600,  transform=ax.transAxes)

generate_top_text(0, "Profit ALL", '256%')
generate_top_text(0.1, "MaxDD", '16%')
generate_top_text(0.2, "Total Age", '365 days')
generate_top_text(0.52, "CAGR%", '19%')
generate_top_text(0.61, "Av. Mounthly", '23%')
generate_top_text(0.74, "Av. Daily Profit", '23%')
generate_top_text(0.89, 'Net Pnl', '23%')
generate_top_text(1, "Win Ratio", '23%')

# plt.text(0, 220, "Profit ALL", fontsize='large')
# plt.text(0, 200, "256%", fontsize='x-large', fontweight=600)

# plt.text(1.5, 220, "MaxDD", fontsize='large')
# plt.text(1.5, 200, "16%", fontsize='x-large', fontweight=600)

# plt.text(3, 220, "Total Age", fontsize='large')
# plt.text(3, 200, "365 days", fontsize='x-large', fontweight=600)

# plt.text(7, 220, "CAGR%", fontsize='large')
# plt.text(7, 200, "19%", fontsize='x-large', fontweight=600)

# plt.text(8, 220, "Av. Mounth", fontsize='large')
# plt.text(8, 200, "23%", fontsize='x-large', fontweight=600)

# plt.text(9.5, 220, "Av. Daily Profit", fontsize='large')
# plt.text(9.5, 200, "23%", fontsize='x-large', fontweight=600)

# plt.text(11.5, 220, "PnL ratio", fontsize='large')
# plt.text(11.5, 200, "23%", fontsize='x-large', fontweight=600)

# plt.text(13, 220, "Win Ratio", fontsize='large')
# plt.text(13, 200, "23%", fontsize='x-large', fontweight=600)

# plt.text(13, 220, "Win Ratio", fontsize='large')
# plt.text(13, 200, "23%", fontsize='x-large', fontweight=600)



plt.text(0.91, 1.68, "owned by", fontsize='small', color='gray', transform=ax.transAxes)
plt.text(0.93, 1.58, "user", fontsize='small', fontweight=500, transform=ax.transAxes)

def generate_text(position, month):
  plt.text(position, -0.15, "-40%", fontsize='medium', color='#F16F5D', transform=ax.transAxes)
  plt.text(position, -0.27, "100%", fontsize='medium', color='#09B978', transform=ax.transAxes)
  plt.text(position, -0.42, month, fontsize='medium', color='#00000080', transform=ax.transAxes)


plt.text(0, -0.15, "2019", fontsize='medium', color='#000000bf', fontweight=600, transform=ax.transAxes)
plt.text(0, -0.27, "2020", fontsize='medium', color='#000000bf', fontweight=600, transform=ax.transAxes)
constant = 0.95
generate_text(constant/size, 'Jan')
generate_text(2*constant/size, 'Feb')
generate_text(3*constant/size, 'Mar')
generate_text(4*constant/size, 'Apr')
generate_text(5*constant/size, 'May')
generate_text(6*constant/size, 'Jun')
generate_text(7*constant/size, 'Jul')
generate_text(8*constant/size, 'Aug')
generate_text(9*constant/size, 'Sep')
generate_text(10*constant/size, 'Oct')
generate_text(11*constant/size, 'Nov')
generate_text(12*constant/size, 'Dec')
generate_text(1.01, 'Annual')

#ploting
plt.plot(xnew , y_smooth, color="#ED932E", linewidth=2)
# plt.savefig('test.svg')
plt.show()