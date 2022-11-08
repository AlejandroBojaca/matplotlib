import numpy as np
import pandas as pd
import json

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so
from matplotlib import rcParams


info = {
  "chartType": "dark-profit-chart",
  "chartData": {
    "profits": [0, 1.23, 5.34, 15.4, 54.1, 146.42],
    "timestamps": [0, 1, 2, 3, 4, 5,],
    "userId": "794ee75b-30e8-4941-be45-1f397775985d"
  }
}

info = json.loads(json.dumps(info))
plotingInfo = pd.DataFrame(info["chartData"])

tips = sns.load_dataset('tips')

# print(plotingInfo)
# print(tips)

# sns.set_theme()

# tips = sns.load_dataset("tips")


## DISTRIBUTIAL PLOT

# sns.displot(data=plotingInfo, y="profits", kde=True)

# 300 represents number of points to make between T.min and T.max

sns.relplot(
    data=plotingInfo, 
    kind="line",
    x="timestamps",
    y="profits"
)

# sns.displot(data=tips, x='total_bill', kind='kde')

# fig, ax = plt.subplots(figsize=(12, 5))
# sns.displot(data=plotingInfo,  x='profits', kind='kde', fill=True, ax=ax)


# plt.savefig('test.svg')

# plt.ylabel('some numbers')
# # plt.savefig('test.svg')


plt.show()