# Importing packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs


# Plot 3 clusters
plt.figure('3 varying clusters along vertical axis')
for loc, scale, N, col, mark in zip([0, 2, 4], [1.0, 0.15, 0.125],[10, 10, 10], ['r', 'g', 'b'], ['*', '^', '.']):
    cluster = np.random.normal(loc=loc, scale=scale, size=(N, 1))
    print(cluster.shape)
    plt.scatter(np.arange(N), cluster, c=col, marker= mark)
plt.show()

# Generate some data
X, y_true = make_blobs(n_samples=400, centers=4,
                       cluster_std=0.60, random_state=0)
X = X[:, ::-1] # flip axes for better plotting

# Create KMeans with 4z clusters
model  = KMeans(n_clusters= 4, random_state= 0)

# Fit the model to points
labels = model.fit(X).predict(X)

# Scatter plot
plt.figure('Scatter plot - 4 clusters')
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.show()
