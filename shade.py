import numpy as np
from matplotlib import pyplot as plt

def f(t):
    return t * t

t = np.arange(-4,4,1/40)

#Print the curve
plt.plot(t,f(t))

#Fill under the curve
plt.fill_between(
        x= t, 
        y1= f(t), 
        where= (-1 < t)&(t < 1),
        color= "b",
        alpha= 0.2)
        
plt.show()