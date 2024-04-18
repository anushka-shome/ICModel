# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 15:14:24 2016

@author: Brandon S. Coventry     Purdue CAP Lab
"""
import scipy.io as sio
import numpy as np
from sklearn import svm, datasets
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
import matplotlib.pyplot as plt
from itertools import cycle
#Load in Unit Collection
Unitvector = sio.loadmat('UnitCollection.mat')
#Get rid of the other info collected by sio
Unitvector = Unitvector['Unitvector']
#Seperate data into Features and Labels
Labels = Unitvector[26,:]
Unitvector = np.delete(Unitvector,26,0)
#Get rid of CF data, not a useful feature for this case
Unitvector = np.delete(Unitvector,8,0)
Unitvector = np.transpose(Unitvector)
biofeat = np.zeros([16,8])
for ii in range(8):
    biofeat[:,ii] = Unitvector[:,ii]
C = 1.0     #SVM Regularization parameter
svc = svm.SVC(kernel='linear', C=C)
svc.fit(Unitvector, Labels)
#Try Affinity clustering
af = AffinityPropagation().fit(biofeat)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
n_clusters_ = len(cluster_centers_indices)

print('Estimated number of clusters: %d' % n_clusters_)
plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = biofeat[cluster_centers_indices[k]]
    plt.plot(biofeat[class_members, 0], biofeat[class_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    for x in biofeat[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()