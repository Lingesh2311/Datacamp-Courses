from sklearn.mixture import GMM
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

# Generate some data
X, y_true = make_blobs(n_samples=400, centers=4,
                       cluster_std=0.60, random_state=0)
X = X[:, ::-1]  # flip axes for better plotting

gmm = GMM(n_components=4).fit(X)
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')

# Get the probability of the cluster assignments
probs = gmm.predict_proba(X)
print(probs[:5].round(3))
