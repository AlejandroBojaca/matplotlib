import numpy as np
from matplotlib import pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
profits = np.array([0, 1.23, 5.34, 15.4, 54.1, 146.42, 0, 1.23, 5.34, 15.4, 54.1, 146.42, 5, 4])
zero = [profits.min() - 1] * profits.size 


#Print the curve
plt.plot(time, profits)

#Fill under the curve
plt.fill_between(
        x= time, 
        y1= profits, 
        y2= zero,
        where= (-1 < time)&(time < 15),
        color= "b",
        alpha= 0.2)
        
plt.show()