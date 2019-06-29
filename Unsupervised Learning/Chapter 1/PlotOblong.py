'''
K means has no built-in way of handling for oblong or
elliptical clusters. Consider the following
'''

from Cluster1 import X
import numpy as np
from sklearn.cluster import KMeans
from PlotCluster import plot_kmeans

rng = np.random.RandomState(seed=13)
X_stretched = np.dot(X, rng.randn(2, 2))

kmeans = KMeans(n_clusters=4, random_state=0)
plot_kmeans(kmeans, X_stretched)
