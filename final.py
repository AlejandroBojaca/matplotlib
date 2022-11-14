import numpy as np
import pandas as pd
import json

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
from scipy.interpolate import make_interp_spline

with open('data.json') as json_file:
    data = json.load(json_file)

profits = np.array(data['chartData']['profits'])
number_profits = profits.size
x = np.array([col for col in range(number_profits)])
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
username = "User"[:9]
portfolio_name = 'test'
chart_type = data['chartType']
background_color = '#FFFFFF' if chart_type == 'standart-profit-chart' else "#000000"
line_color = '#ED932E' if chart_type == 'standart-profit-chart' else '#F1AA01'
main_text_color = '#000000' if chart_type == 'standart-profit-chart' else '#FFFFFF'
second_text_color = '#000000bf' if chart_type == 'standart-profit-chart' else '#ffffffbf'
third_text_color = '#00000080' if chart_type == 'standart-profit-chart' else '#ffffff80'
negative_prof_color = '#F16F5D' 
positive_prof_color = '#09B978' 
width = 1024
height = 512
linewidth=2
extra_points = 150
plt.rcParams['font.family'] = 'roboto'
px = 1/plt.rcParams['figure.dpi']

#create smooth line chart 
xnew = np.linspace(x.min(), x.max(), extra_points)
spl = make_interp_spline(x, profits, k=2)
profits_smooth = spl(xnew)
bottom_plot = np.array([profits_smooth.min() - 1] * profits_smooth.size)

#resize
fig = plt.figure(figsize=(width*px, height*px), facecolor=background_color)
plt.subplots_adjust(top=0.63, bottom=0.23, left=0.05, right=0.89)

#images
portfolio_name_width = fig.text(-100, -100, portfolio_name, visible=True).get_window_extent(renderer=fig.canvas.get_renderer()).width

binance_logo = plt.imread(get_sample_data('binance_logo.png'))
newax = fig.add_axes([0.05+(portfolio_name_width*0.00172), 0.89, 0.04, 0.04])
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

#backgroundcolor and ticks
ax = plt.axes()
ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
plt.tick_params(
    axis='both',          
    which='both',      
    bottom=False,
    left=False, 
    right=False,
    labelbottom=False,
    labelright=True,
    labelleft=False,
    pad=5,
    labelcolor=third_text_color,
    labelsize='small'
    )
plt.margins(x=0)
ax.set_facecolor(background_color)
ax.yaxis.set_major_formatter('{x:1.0f}%')

#shade
plt.fill_between(
        x= xnew, 
        y1= profits_smooth, 
        y2= bottom_plot,
        where= (-min(xnew) <= xnew)&(xnew <= max(xnew)),
        color= line_color,
        alpha= 0.2)

#add texts
plt.text(0, 1.66, portfolio_name, fontsize='xx-large',color=main_text_color, fontweight=500, transform=ax.transAxes)
plt.text(0, 1.55, "TradeLink portfolio • tracking for 35 days since Jan 01, 2020", fontsize='small', color=third_text_color, transform=ax.transAxes)

def generate_top_text(position, top_text, bottom_text): 
  plt.text(position, 1.25, top_text, fontsize='medium', color=second_text_color,  transform=ax.transAxes)
  plt.text(position, 1.1, bottom_text, fontsize='x-large',color=main_text_color, fontweight=600,  transform=ax.transAxes)

generate_top_text(0, "Profit ALL", '256%')
generate_top_text(0.1, "MaxDD", '16%')
generate_top_text(0.2, "Total Age", '365 days')
generate_top_text(0.52, "CAGR%", '19%')
generate_top_text(0.61, "Av. Mounthly", '23%')
generate_top_text(0.74, "Av. Daily Profit", '23%')
generate_top_text(0.89, 'Net Pnl', '23%')
generate_top_text(1, "Win Ratio", '23%')

plt.text(0.91, 1.68, "owned by", fontsize='small', color=third_text_color, transform=ax.transAxes)
plt.text(0.93, 1.58, username, fontsize='small', color=second_text_color, fontweight=500, transform=ax.transAxes, )

def generate_text(position, month):
  plt.text(position, -0.15, "-40%", fontsize='medium', color=negative_prof_color, transform=ax.transAxes)
  plt.text(position, -0.27, "100%", fontsize='medium', color=positive_prof_color, transform=ax.transAxes)
  plt.text(position, -0.42, month, fontsize='medium', color=third_text_color, transform=ax.transAxes)


plt.text(0, -0.15, "2019", fontsize='medium', color=third_text_color, fontweight=600, transform=ax.transAxes)
plt.text(0, -0.27, "2020", fontsize='medium', color=third_text_color, fontweight=600, transform=ax.transAxes)
x_limit = 0.95
for i in range(number_profits):
    generate_text((i+1)*x_limit/number_profits, months[i])
generate_text(1.03, 'Annual')

plt.plot(xnew , profits_smooth, color=line_color, linewidth=linewidth)
# plt.savefig('test.svg')
plt.show()
