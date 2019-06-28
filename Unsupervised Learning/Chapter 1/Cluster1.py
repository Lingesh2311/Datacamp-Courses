# Importing packages
import numpy as np
import matplotlib.pyplot as plt

N = 20 # Number of points in each cluster
k = 3 # Number of clusters
points = np.random.normal(loc=[0, 1, 2], scale=[0.5, 0.75, 1.0], size=(N, k))

print(points)

# Plotting the clusters
