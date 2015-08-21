'''
Created on 2015. 7. 1.

@author: user
'''

from numpy import *
from fileinput import filename
import scipy.stats as ss

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

def getPCAColumnNum(dataMat, topNfest = 9999999):
    tmp = []
    meanMtx = []
    transformedMtx = []
    arrayNum = len(list(dataMat[0][0]))
    for tmpIndex in range(0, len(dataMat)):
    #     for tmpII in range(0,dataMat[tmpIndex].len()):
        meanMtx.append([0 for _ in range(arrayNum)])
        tmp.append([])
        for timeIndex in range(0,len(dataMat[tmpIndex])):
            tmp[tmpIndex].append(list(dataMat[tmpIndex][timeIndex]))
            for arrayIndex in range(0, arrayNum):
                meanMtx[tmpIndex][arrayIndex] += tmp[tmpIndex][timeIndex][arrayIndex]
        
    
    for tmpIndex in range(0, len(dataMat)):
        for arrayIndex in range(0, arrayNum):
            meanMtx[tmpIndex][arrayIndex] = meanMtx[tmpIndex][arrayIndex] / len(dataMat[tmpIndex])
        
        for timeIndex in range(0, len(dataMat[tmpIndex])):
            for arrayIndex in range(0, arrayNum):
                tmp[tmpIndex][timeIndex][arrayIndex] = tmp[tmpIndex][timeIndex][arrayIndex] - meanMtx[tmpIndex][arrayIndex]
    # time inde
    
    
    for timeIndex in range(0, len(dataMat[0])):
        transformedMtx.append([])
        
        for arrayIndex in range(0, arrayNum):
            transformedMtx[timeIndex].append([])
            
            for stockIndex in range(0, len(dataMat)):
                transformedMtx[timeIndex][arrayIndex].append([])
                transformedMtx[timeIndex][arrayIndex][stockIndex] = tmp[stockIndex][timeIndex][arrayIndex]
    
    CovMat = zeros((arrayNum, arrayNum), float)
    
    for time in range(0, len(transformedMtx)):
        for i in range(0, arrayNum):
            for j in range(0, arrayNum):
                tempSum = 0
                for stockIndex in range(0, len(dataMat)):
                    tempSum += transformedMtx[time][i][stockIndex] * transformedMtx[time][j][stockIndex]
                CovMat[i][j] += tempSum
    
                
    CovMat = [x / len(transformedMtx) for x in CovMat]
    eigVals, eigVects = linalg.eig(mat(CovMat))
    tteemmpp = ss.rankdata(eigVals)
    print(tteemmpp)
    tteemmppColumnNum = []
    for index in range(0, len(eigVals)):
        if tteemmpp[index] > (len(eigVals) - topNfest) :
            tteemmppColumnNum.append(index)
            
    return tteemmppColumnNum