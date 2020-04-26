from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

dataset = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.6, random_state=50)
dataset_points = dataset[0]
plt.scatter(dataset[0][:, 0], dataset[0][:, 1], c=dataset[1], cmap='viridis')
plt.xlim(-15, 15)
plt.ylim(-15, 15)
