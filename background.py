import matplotlib.pyplot as plt
import numpy as np
  
# giving values for x and y to plot
x = np.arange(0, 10, .1)
y = np.sin(x)
  
# Set background color of the outer 
# area of the plt
plt.figure(facecolor='yellow')
  
# Plotting the graph between x and y
plt.plot(x, y)
  
# Giving x label using xlabel() method
# with bold setting
plt.xlabel("X")
ax = plt.axes()
  
# Setting the background color of the plot 
# using set_facecolor() method
ax.set_facecolor("yellow")
  
# Giving y label using xlabel() method with
# bold setting
plt.ylabel('sin(x)')
  
# Showing the plot using plt.show()
plt.show()