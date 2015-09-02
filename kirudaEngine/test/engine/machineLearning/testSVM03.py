#-*- coding: utf-8 -*-
'''
Created on 2015. 8. 19.

@author: Jay
'''
from sklearn import svm
from engine.portfolio.SelectAssets import SelectAsset
from sklearn.preprocessing.data import StandardScaler, Normalizer
from engine.data.TrainingData import TrainingData
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from util.schedule.Vertex import Vertex
from util.schedule.Date import Date
from engine.type.PortfolioType import PortfolioType
from engine.type.TrainingDataType import TrainingDataType

calendar = SouthKoreaCalendar(1)
#ASSETS
sa = SelectAsset()
variables = [PortfolioType.MARKET, PortfolioType.DESIGNATED, PortfolioType.MARKETCAP]
conditions = ["='KS'", "='N'", ">=1000000"]
assets = sa.select(variables, conditions, Date("20150601"))
#assets = sa.selectTest()
print len(assets)

#DATA
datasForX = [
    TrainingDataType.DataEnum.ClosePrice, 
    TrainingDataType.DataEnum.TradingVolume,
    TrainingDataType.DataEnum.MarketCap,
    TrainingDataType.DataEnum.ForeignHoldingStock,
]
dataTypesForX = [
    TrainingDataType.TypeEnum.RateOfChange, 
    TrainingDataType.TypeEnum.RateOfChange,
    TrainingDataType.TypeEnum.Value,
    TrainingDataType.TypeEnum.Value,
]
dataCondiTypesForX = [
    TrainingDataType.ConditionEnum.NONE, 
    TrainingDataType.ConditionEnum.LAG,
    TrainingDataType.ConditionEnum.NONE,
    TrainingDataType.ConditionEnum.NONE,
]
dataConditionsForX = [
    -1, 
    -1,
    0,
    0,
]

#########################TRAINING SET###################################

#PERIOD
asOfDate = Date("20150301")
vtx = Vertex.valueOf("M6")
lagTime = 7

tData = TrainingData(assets, calendar, datasForX, dataTypesForX, dataCondiTypesForX, dataConditionsForX)
tData.genTrainingXData(asOfDate, vtx)
tData.genTrainingYData(asOfDate, lagTime, tData.getNumOfPeriod())

################################Test Set##################################
#PERIOD
#asOfDate = Date("20150617")
vtxOfTestSet = Vertex.valueOf("D0")
lagTime= 7
#DATA
tDataOfTestSET = TrainingData(assets, calendar, datasForX, dataTypesForX, dataCondiTypesForX, dataConditionsForX)

tDataOfTestSET.genTrainingXData(asOfDate.plusDays(1), vtxOfTestSet)
tDataOfTestSET.genTrainingYData(asOfDate.plusDays(1), lagTime, tDataOfTestSET.getNumOfPeriod())

######################################ML #####################################
X = tData.getX()
Y = tData.getY()
testX = tDataOfTestSET.getX()
testY = tDataOfTestSET.getY()

totalTime = 90

prob1 = [[] for _ in range(len(assets))]
prob2 = [[] for _ in range(len(assets))]
prob3 = [[] for _ in range(len(assets))]
for timeIndex in range(0, totalTime) :        
    for stockIndex in range(0, len(assets)) :        
        #print assets[stockIndex].getAssetName(),assets[stockIndex].getAssetCode()
        #print testY[stockIndex]
        #print X[stockIndex]
        scaledX = StandardScaler().fit_transform(X[stockIndex])
        C = 10.0  # SVM regularization parameter
        svc = svm.SVC(kernel='linear', C=C).fit(scaledX, Y[stockIndex])
        rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(scaledX, Y[stockIndex])
        ##poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X[stockIndex], y[stockIndex])
        lin_svc = svm.LinearSVC(C=C).fit(scaledX, Y[stockIndex])
        
        for i, clf in enumerate((svc, lin_svc, rbf_svc)) :#, poly_svc)):
            
            testScaledX = testX[stockIndex]
            #print testX[stockIndex]
            Z = clf.predict(testScaledX)
            #K = clf.cross_validation(X,y)
            #print (clf)
            #print (Z)
            
            stringTMP = ""
            sum = 0
            idx = 0
            for kk in Z :
                stringTMP = stringTMP + repr(kk) + ", "
                if testY[stockIndex][idx] == kk :
                    sum = sum + 1            
                idx = idx + 1
            #print clf
            if i == 0 :
                prob1[stockIndex].append(sum)
            elif i == 1 :
                prob2[stockIndex].append(sum)
            elif i == 2 :
                prob3[stockIndex].append(sum)
            #print stringTMP , sum
              
        #print assets[stockIndex].getAssetName(),assets[stockIndex].getAssetCode(), prob[0], prob[1], prob[2]
        
    asOfDate = asOfDate.plusDays(1)
    X = tData.genNextX(asOfDate)
    Y = tData.genNextY(asOfDate)
    
    testX = tDataOfTestSET.genNextX(asOfDate.plusDays(1))
    testY = tDataOfTestSET.genNextY(asOfDate.plusDays(1))

print prob1
print prob2
print prob3

for stockIndex in range(0, len(prob1)) :
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for index in range(0, len(prob1[stockIndex])):
        sum1 = sum1 + prob1[stockIndex][index]
        sum2 = sum2 + prob2[stockIndex][index]
        sum3 = sum3 + prob3[stockIndex][index]
    print assets[stockIndex].getAssetName(),assets[stockIndex].getAssetCode(), \
            float(sum1)/float(totalTime),\
            float(sum2)/float(totalTime),\
            float(sum3)/float(totalTime)
    
