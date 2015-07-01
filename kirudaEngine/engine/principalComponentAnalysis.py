'''
Created on 2015. 7. 1.

@author: user
'''

from numpy import *
from fileinput import filename


def pca(dataMat, topNfeat = 9999999):
    meanVals = mean(dataMat, axis = 0)
    meanRemoved = dataMat - meanVals
    covMat = cov(meanRemoved, meanVals)
    eigVals, eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat + 1): -1]
    redEigVects = eigVects[:,eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat


# http://quant.stackexchange.com/questions/7868/how-to-use-pca-for-trading
# def getStockSisaeData(self, assetLists, periods):
#         
#         sisaeTable = []
#         for assetIndex in range(0, len(assetLists)):
#             assetCode = assetLists[assetIndex].getAssetCode()
#             tmpList = []
#             timeStatement = ""
#             for timeIndex in range(0, len(periods)):
#                 date = periods[timeIndex]   
#                 tmp = " DATE = '" + date + "' OR"                 
#                 timeStatement = timeStatement + tmp
# #             conditionStatement = "marketCap >= " + condition
#             
#             totalStatement = sqlMap.SELECTHISTORICALSTOCKSISAE %(assetCode, timeStatement[:-2])
#             sisae = self.dbInstance.select(totalStatement)
#             
#             for timeIndex in range(0, len(periods)):
#                 if periods[timeIndex] == sisae[timeIndex][1]:
#                     tmpList.append(sisae[timeIndex][2:10])
#                 else :
#                     tmpList.append(0)
#             
#             sisaeTable.append(tmpList)
#         return sisaeTable



# SELECTHISTORICALSTOCKSISAE = "\
#         SELECT \
#             * \
#         FROM \
#             STOCK_SISAE \
#         WHERE \
#             CODE = '%s' \
#             AND (%s) "