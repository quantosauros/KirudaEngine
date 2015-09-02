#-*- coding: utf-8 -*-
'''
Created on 2015. 7. 24.

@author: Jay
'''
from sklearn import cluster
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from engine.selectAssets import SelectAsset
from engine.historicalData import HistoricalData
import numpy as np
from engine.type.PortfolioType import PortfolioType

#Assets
sa = SelectAsset()
variables = [PortfolioType.MARKET]
conditions = ["='KS'"]
assets = sa.select(variables, conditions)
#assets = sa.selectTest()
assetCodeSTR = ""
assetNameSTR = ""
for asset in assets:
    #print (asset.getAssetCode())
    assetCodeSTR = assetCodeSTR + asset.getAssetCode() + "," 
    assetNameSTR = assetNameSTR + asset.getAssetName() + ","
print (assetCodeSTR)
print (assetNameSTR)

#periods
periods = ['20150102',    '20150105',    '20150106',    '20150107',    '20150108',    '20150109',    '20150112',    '20150113',    '20150114',    '20150115',    '20150116',    '20150119',    '20150120',    '20150121',    '20150122',    '20150123',    '20150126',    '20150127',    '20150128',    '20150129',    '20150130',    '20150202',    '20150203',    '20150204',    '20150205',    '20150206',    '20150209',    '20150210',    '20150211',    '20150212',    '20150213',    '20150216',    '20150217',    '20150223',    '20150224',    '20150225',    '20150226',    '20150227',    '20150302',    '20150303',    '20150304',    '20150305',    '20150306',    '20150309',    '20150310',    '20150311',    '20150312',    '20150313',    '20150316',    '20150317',    '20150318',    '20150319',    '20150320',    '20150323',    '20150324',    '20150325',    '20150326',    '20150327',    '20150330',    '20150331',    '20150401',    '20150402',    '20150403',    '20150406',    '20150407',    '20150408',    '20150409',    '20150410',    '20150413',    '20150414',    '20150415',    '20150416',    '20150417',    '20150420',    '20150421',    '20150422',    '20150423',    '20150424',    '20150427',    '20150428',    '20150429',    '20150430',    '20150504',    '20150506',    '20150507',    '20150508',    '20150511',    '20150512',    '20150513',    '20150514',    '20150515',    '20150518',    '20150519',    '20150520',    '20150521',    '20150522',    '20150526',    '20150527',    '20150528',    '20150529',    '20150601',    '20150602',    '20150603',    '20150604',    '20150605',    '20150608',    '20150609',    '20150610',    '20150611',    '20150612',    '20150615',    '20150616',    '20150617',    '20150618']


#Historical Prices
hd = HistoricalData()
sisae = hd.getStockSisaeData(assets, periods)
#print(len(sisae))
#print(sisae)

X = []
for index in range(0, len(sisae)):
    tt = []
    for timeIndex in range(0, len(sisae[index])) :
        tt = tt + sisae[index][timeIndex]        
    X.append(tt)


#===============================================================================
# strR = ""
# for xxx in X:
#     #print xxx
#     #print type(xxx)
#     tmpSTRING = ""
#     for i in range(0, len(xxx)):
#         tmpSTRING = tmpSTRING + repr(xxx[i]) + "; " 
#     print(tmpSTRING)
#===============================================================================

X = StandardScaler().fit_transform(X)

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
two_means = cluster.MiniBatchKMeans(n_clusters=100)
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
       
    #print (algorithm)
    stringResult = ""
    for xx in y_pred:
        stringResult = stringResult + repr(xx) + ", "
    print (stringResult)
       
