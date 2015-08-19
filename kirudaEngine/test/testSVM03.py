#-*- coding: utf-8 -*-
'''
Created on 2015. 8. 19.

@author: Jay
'''
from sklearn import svm
from util.Date import Date
from util.SouthKoreaCalendar import SouthKoreaCalendar
from util.Period import Period
from util.Vertex import Vertex
from engine.selectAssets import SelectAsset
from util.assetConditions import assetConditions
from util.dataEnums import dataEnums
from engine.data.AbstractData import AbstractData
from sklearn.preprocessing.data import StandardScaler, Normalizer
from engine.TrainingData import TrainingData


calendar = SouthKoreaCalendar(1)

#ASSETS
sa = SelectAsset()
variables = [assetConditions.MARKET, assetConditions.DESIGNATED, assetConditions.MARKETCAP]
conditions = ["='KS'", "='N'", ">=1000000"]
assets = sa.select(variables, conditions, Date("20150601"))
#assets = sa.selectTest()
print len(assets)

#DATA
datasForX = [
    dataEnums.DataEnum.ClosePrice, 
    dataEnums.DataEnum.TradingVolume,
    dataEnums.DataEnum.MarketCap,
    dataEnums.DataEnum.ForeignHoldingStock,
]
dataTypesForX = [
    dataEnums.TypeEnum.RateOfChange, 
    dataEnums.TypeEnum.RateOfChange,
    dataEnums.TypeEnum.Value,
    dataEnums.TypeEnum.Value,
]
dataCondiTypesForX = [
    dataEnums.ConditionEnum.NONE, 
    dataEnums.ConditionEnum.LAG,
    dataEnums.ConditionEnum.NONE,
    dataEnums.ConditionEnum.NONE,
]
dataConditionsForX = [
    -1, 
    -1,
    0,
    0,
]

#########################TRAINING SET###################################

#PERIOD
asOfDate = Date("20150601")
vtx = Vertex.valueOf("M6")
lagTime = 7

tData = TrainingData(assets, datasForX, dataTypesForX, dataCondiTypesForX, dataConditionsForX)
X = tData.getTrainingXData(asOfDate, calendar, vtx)
print len(X[0])
y = tData.getTrainingYData(asOfDate, calendar, lagTime, len(X[0]))

################################Test Set##################################
#PERIOD
asOfDate = Date("20150617")
vtxOfTestSet = Vertex.valueOf("D1")
lagTime= 7
#DATA
tDataOfTestSET = TrainingData(assets, datasForX, dataTypesForX, dataCondiTypesForX, dataConditionsForX)

testX = tDataOfTestSET.getTrainingXData(asOfDate, calendar, vtxOfTestSet)
testY = tDataOfTestSET.getTrainingYData(asOfDate, calendar, lagTime, len(testX[0]))

######################################ML #####################################
for index in range(0, len(assets)) :
    
    print assets[index].getAssetName(),assets[index].getAssetCode()
    #print testY[index]
    print X[index]
    scaledX = StandardScaler().fit_transform(X[index])
    C = 10.0  # SVM regularization parameter
    svc = svm.SVC(kernel='linear', C=C).fit(scaledX, y[index])
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(scaledX, y[index])
    ##poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X[index], y[index])
    lin_svc = svm.LinearSVC(C=C).fit(scaledX, y[index])
    
    #testX = X[index]        
    
    prob = []    
    for i, clf in enumerate((svc, lin_svc, rbf_svc)) :#, poly_svc)):
        
        testScaledX = testX[index]
        #print testX[index]
        Z = clf.predict(testScaledX)
        #K = clf.cross_validation(X,y)
        #print (clf)
        #print (Z)
        
        stringTMP = ""
        sum = 0
        idx = 0
        for kk in Z :
            stringTMP = stringTMP + repr(kk) + ", "
            if testY[index][idx] == kk :
                sum = sum + 1            
            idx = idx + 1
        #print clf
        prob.append(float(sum)/float(len(testY[index])))
        #print stringTMP , sum
          
    print assets[index].getAssetName(),assets[index].getAssetCode(), prob[0], prob[1], prob[2]
    #print prob[0], prob[1], prob[2]

