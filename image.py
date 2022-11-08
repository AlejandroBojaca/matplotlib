import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data

T = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
power = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])

im = plt.imread(get_sample_data('C://Users/david/Desktop/matplotlib/binance_logo.png'))

fig, ax = plt.subplots()
# ax.plot(range(10))

newax = fig.add_axes([0.1, 0.9, 0.1, 0.2], anchor='NE', zorder=-1)
newax.imshow(im)
newax.axis('off')

ax.plot(T , power)
plt.text(-2, 160, "Profit ALL\n256%", fontsize='xx-large')
plt.text(2, 160, "MaxDD\n16%", fontsize='xx-large')
plt.show()