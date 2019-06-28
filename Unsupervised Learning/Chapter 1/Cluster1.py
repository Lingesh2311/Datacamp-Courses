# Importing packages
import numpy as np
import matplotlib.pyplot as plt

# Plot 3 clusters
for loc, scale, N, col, mark in zip([0, 2, 4], [1.0, 0.5, 0.25],[10, 30, 40], ['r', 'g', 'b'], ['*', '^', '.']):
    print(N)
    cluster = np.random.normal(loc=loc, scale=scale, size=(N, 1))
    plt.scatter(np.arange(N), cluster, c=col, marker= mark)
plt.show()
