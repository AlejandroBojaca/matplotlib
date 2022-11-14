import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data

T = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
power = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])

im = plt.imread(get_sample_data('binance_logo.png'))

fig = plt.figure(figsize=(13, 6))
plt.subplots_adjust(top=0.6, bottom=0.2, left=0, right=0.95)
ax = plt.axes()


r = fig.canvas.get_renderer()
t = plt.text(0.5, 0.5, 'T')

bb = t.get_window_extent(renderer=r)
width = bb.width
height = bb.height

print(width, height)



newax = fig.add_axes([0, 0.8, 0.1, 0.1], anchor='NE', zorder=1)
newax.imshow(im)
newax.axis('off')
newax = fig.add_axes([0.8 ,0.8, 0.1, 0.1], anchor='NE', zorder=1)
newax.imshow(im)
newax.axis('off')
plt.show()