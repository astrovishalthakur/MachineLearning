import random
import numpy as np


def move_centroids(x, cluster_group):
    new_centroids = []

    # extract unique clusters
    cluster_type = np.unique(cluster_group)

    for type_name in cluster_type:
        new_centroids.append(x[cluster_group == type_name].mean(axis=0))

    return np.array(new_centroids)


class KMeans:
    def __init__(self, n_clusters=2, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit_predict(self, x):
        random_index = (random.sample(range(0, x.shape[0]), self.n_clusters))
        self.centroids = x[random_index]

        for i in range(self.max_iter):
            # Assign clusters
            cluster_group = self.assign_clusters(x)

            # move centroids
            old_centroids = self.centroids
            self.centroids = move_centroids(x, cluster_group)

            # check finish
            if (old_centroids == self.centroids).all():
                break
        return cluster_group

    def assign_clusters(self, x):
        cluster_group = []
        distances = []

        for row in x:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row - centroid, row - centroid)))
            min_distance = min(distances)
            index_pos = distances.index(min_distance)
            cluster_group.append(index_pos)
            distances.clear()
        return np.array(cluster_group)
