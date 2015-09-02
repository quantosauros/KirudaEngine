#-*- coding: utf-8 -*-
'''
Created on 2015. 7. 1.

@author: user
'''
from engine.portfolio.HistoricalData import HistoricalData
from engine.portfolio.SelectAssets import SelectAsset
from engine.type.PortfolioType import PortfolioType
from engine.portfolio.Portfolio import Portfolio
from engine.machineLearning.principalComponentAnalysis import pca, getPCAColumnNum
from numpy import zeros

#Assets
sa = SelectAsset()
assets = sa.selectTest()
#print(assets)
variables = [PortfolioType.MARKET]
conditions = ["='KS'"]
#variables = [assetConditions.MARKET, assetConditions.MARKETCAP]
#conditions = ["='KS'", ">'5000'"]
assets = sa.select(variables, conditions)
#for x in assets:
#    print(x)
periods = ['20150610', '20150611', '20150612', '20150615', '20150616', '20150617', '20150618']
#periods = ['20150617', '20150618']
hd = HistoricalData()
sisae = hd.getStockSisaeData1(assets, periods)

#print(sisae)

dd = getPCAColumnNum(sisae, topNfest = 10)
print(dd)
# 
# tmp = []
# meanMtx = []
# transformedMtx = []
# arrayNum = len(list(sisae[0][0]))
# for tmpIndex in range(0, len(sisae)):
# #     for tmpII in range(0,sisae[tmpIndex].len()):
#     meanMtx.append([0 for _ in range(arrayNum)])
#     tmp.append([])
#     for timeIndex in range(0,len(sisae[tmpIndex])):
#         tmp[tmpIndex].append(list(sisae[tmpIndex][timeIndex]))
#         for arrayIndex in range(0, arrayNum):
#             meanMtx[tmpIndex][arrayIndex] += tmp[tmpIndex][timeIndex][arrayIndex]
#     
# 
# for tmpIndex in range(0, len(sisae)):
#     for arrayIndex in range(0, arrayNum):
#         meanMtx[tmpIndex][arrayIndex] = meanMtx[tmpIndex][arrayIndex] / len(sisae[tmpIndex])
#     
#     for timeIndex in range(0, len(sisae[tmpIndex])):
#         for arrayIndex in range(0, arrayNum):
#             tmp[tmpIndex][timeIndex][arrayIndex] = tmp[tmpIndex][timeIndex][arrayIndex] - meanMtx[tmpIndex][arrayIndex]
# # time inde
# 
# 
# for timeIndex in range(0, len(sisae[0])):
#     transformedMtx.append([])
#     
#     for arrayIndex in range(0, arrayNum):
#         transformedMtx[timeIndex].append([])
#         
#         for stockIndex in range(0, len(sisae)):
#             transformedMtx[timeIndex][arrayIndex].append([])
#             transformedMtx[timeIndex][arrayIndex][stockIndex] = tmp[stockIndex][timeIndex][arrayIndex]
# 
# CovMat = zeros((arrayNum, arrayNum), float)
# 
# for time in range(0, len(transformedMtx)):
#     for i in range(0, arrayNum):
#         for j in range(0, arrayNum):
#             tempSum = 0
#             for stockIndex in range(0, len(sisae)):
#                 tempSum += transformedMtx[time][i][stockIndex] * transformedMtx[time][j][stockIndex]
#             CovMat[i][j] += tempSum
# 
#             
# CovMat = [x / len(transformedMtx) for x in CovMat]
#         
# dd = pca(transformedMtx, 4)
# pfo = Portfolio(assets, [1,],0)


