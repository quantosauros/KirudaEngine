import numpy as np
from sklearn import cluster, datasets
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
import csv

# Generate datasets. We choose the size big enough to see the scalability
# of the algorithms, but not too big to avoid too long running times
#n_samples = 1500
#noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5,
#                                      noise=.05)

trainingMtx = []
f = open('D:\\trainingData.csv','r')
trainingData = csv.reader(f)
for row in trainingData:
#     tmpArray = row.split(',')
    tmpArray = map(float, row)
    trainingMtx.append(tmpArray)

#X, y = noisy_circles
X = trainingMtx
strR = ""
for xxx in X:
    tmpSTRING = ""
    for i in range(0, len(xxx)):
        tmpSTRING = tmpSTRING + repr(xxx[i]) + "; " 
        
    strR = strR + "[" + tmpSTRING + "], "
print strR
#print (y)
X = StandardScaler().fit_transform(X)
strR = ""
for xxx in X:
    tmpSTRING = ""
    for i in range(0, len(xxx)):
        tmpSTRING = tmpSTRING + repr(xxx[i]) + "; " 
        
    strR = strR + "[" + tmpSTRING + "], "
print strR


clustering_names = [
    'MiniBatchKMeans', 'AffinityPropagation', 'MeanShift',
    'SpectralClustering', 'Ward', 'AgglomerativeClustering',
    'DBSCAN', 'Birch']

# estimate bandwidth for mean shift
bandwidth = cluster.estimate_bandwidth(X, quantile=0.3)

# connectivity matrix for structured Ward
connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
# make connectivity symmetric
connectivity = 0.5 * (connectivity + connectivity.T)

# create clustering estimators
ms = cluster.MeanShift(bandwidth=bandwidth, bin_seeding=True)
two_means = cluster.MiniBatchKMeans(n_clusters=2)
ward = cluster.AgglomerativeClustering(n_clusters=2, linkage='ward',
                                       connectivity=connectivity)
spectral = cluster.SpectralClustering(n_clusters=2,
                                      eigen_solver='arpack',
                                      affinity="nearest_neighbors")
dbscan = cluster.DBSCAN(eps=.2)
affinity_propagation = cluster.AffinityPropagation(damping=.9,
                                                   preference=-200)

average_linkage = cluster.AgglomerativeClustering(
    linkage="average", affinity="cityblock", n_clusters=2,
    connectivity=connectivity)

birch = cluster.Birch(n_clusters=2)

clustering_algorithms = [
    two_means, affinity_propagation, ms, spectral, ward, average_linkage,
    dbscan, birch]

for name, algorithm in zip(clustering_names, clustering_algorithms):
    # predict cluster memberships    
    algorithm.fit(X)
    
    if hasattr(algorithm, 'labels_'):
        y_pred = algorithm.labels_.astype(np.int)
    else:
        y_pred = algorithm.predict(X)
    
    print (algorithm)
    stringResult = ""
    for xx in y_pred:
        stringResult = stringResult + repr(xx) + ", "
    print (stringResult)
    