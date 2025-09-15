import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# https://habr.com/ru/articles/748282/
# https://matplotlib.org/stable/users/explain/figure/figure_intro.html

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.
