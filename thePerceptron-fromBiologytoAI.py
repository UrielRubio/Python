# -*- coding: utf-8 -*-
#https://towardsdatascience.com/from-biology-to-ai-the-perceptron-81abfdc788bf



# Import libraries 
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

# Generate dataset
X, Y = make_blobs(n_features=2, centers=2, n_samples=1000, random_state=18)

# Visualize dataset
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.scatter(X[:, 0], X[:, 1], c=Y)
ax.set_title('ground truth', fontsize=20)
plt.show()
