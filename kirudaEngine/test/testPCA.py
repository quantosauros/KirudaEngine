'''
Created on 2015. 7. 1.

@author: user
'''
from engine.assets import Asset
from engine.historicalData import HistoricalData
from engine.selectAssets import SelectAsset
from util.assetConditions import assetConditions
from engine.portfolio import Portfolio
from engine.principalComponentAnalysis import pca
#Assets
sa = SelectAsset()
assets = sa.selectTest()
#print(assets)
variables = [assetConditions.MARKET]
# conditions = ["='KS'"]
variables = [assetConditions.MARKET, assetConditions.MARKETCAP]
conditions = ["='KS'", ">'5000'"]
assets = sa.select(variables, conditions)
for x in assets:
    print(x)
periods = ["20150617", '20150618']
hd = HistoricalData()
sisae = hd.getStockSisaeData(assets, periods)

tmpMerge = []
for tmpIndex in range(0, len(sisae)):
#     for tmpII in range(0,sisae[tmpIndex].len()):
    tmp = sisae[tmpIndex][0] + sisae[tmpIndex][1] 
    tmpList = list(tmp)
    tmpMerge.append(tmpList)
        
dd = pca(tmpMerge, 4)
pfo = Portfolio(assets, [1,],0)

