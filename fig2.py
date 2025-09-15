import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2,2)             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.
