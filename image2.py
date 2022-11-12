import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png
from matplotlib.cbook import get_sample_data

im = read_png('binance logo.png')

fig, ax = plt.subplots()
ax.set_xlim([0, 1000])
ax.set_ylim([0, 1000])

imagebox_python = OffsetImage(im, zoom=".05")
xy= [100, 200]

ab_pythonlogo = AnnotationBbox(imagebox_python, xy, xybox=(30., -30), boxcoords="offset points")
ax.add_artist(ab_pythonlogo)

plt.show()

