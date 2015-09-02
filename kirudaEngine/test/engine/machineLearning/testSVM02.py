#-*- coding: utf-8 -*-
'''
Created on 2015. 8. 19.

@author: Jay
'''
from sklearn import svm
from engine.portfolio.SelectAssets import SelectAsset
from engine.data.AbstractData import AbstractData
from sklearn.preprocessing.data import StandardScaler, Normalizer
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from util.schedule.Period import Period
from util.schedule.Vertex import Vertex
from util.schedule.Date import Date
from engine.type.PortfolioType import PortfolioType
from engine.type.TrainingDataType import TrainingDataType

#PERIOD
asOfDate = Date("20150601")
calendar = SouthKoreaCalendar(1)
pp = Period(asOfDate, calendar)
vtx = Vertex.valueOf("M3")
periods = pp.getPeriodByVertex(vtx)
#for x in periods :
#    print x

#ASSETS
sa = SelectAsset()
variables = [PortfolioType.MARKET, PortfolioType.DESIGNATED, PortfolioType.MARKETCAP]
conditions = ["='KS'", "='N'", ">=1000000"]
assets = sa.select(variables, conditions, asOfDate)
#assets = sa.selectTest()
print len(assets)

#########################TRAINING SET X ###################################
#DATA
dats = [
    TrainingDataType.DataEnum.ClosePrice, 
    TrainingDataType.DataEnum.TradingVolume,
    TrainingDataType.DataEnum.MarketCap,
    TrainingDataType.DataEnum.ForeignHoldingStock,
]
dataTypes = [
    TrainingDataType.TypeEnum.RateOfChange, 
    TrainingDataType.TypeEnum.RateOfChange,
    TrainingDataType.TypeEnum.Value,
    TrainingDataType.TypeEnum.Value,
]
dataCondiTypes = [
    TrainingDataType.ConditionEnum.NONE, 
    TrainingDataType.ConditionEnum.LAG,
    TrainingDataType.ConditionEnum.NONE,
    TrainingDataType.ConditionEnum.NONE,
]
dataConditions = [
    -1, 
    -1,
    0,
    0,
]

dataClass = AbstractData(assets, dats, dataTypes, dataCondiTypes, dataConditions)
result = dataClass.getResult(calendar, periods)

X = []
for stockIndex in range(0, len(result)) :
    tmpX = []
    for dateIndex in range(0, len(result[0])) :
        tmpX.append(result[stockIndex][dateIndex])
    X.append(tmpX)

#######################Training SET Y#################
#PERIOD
asOfDate = asOfDate.plusDays(7)
calendar = SouthKoreaCalendar(1)
pp = Period(asOfDate, calendar)
periods1 = pp.getPeriodByNumber(len(periods))

#for x in periods1 :
#    print x

dats1 = [TrainingDataType.DataEnum.ClosePrice,]
dataTypes1 = [TrainingDataType.TypeEnum.RateOfChange,]
dataCondiTypes1 = [TrainingDataType.ConditionEnum.NONE,]
dataConditions1 = [-7,]

dataClass1 = AbstractData(assets, dats1, dataTypes1, dataCondiTypes1, dataConditions1)
result1 = dataClass1.getResult(calendar, periods1)

y = []
for stockIndex in range(0, len(result1)) :
    tmpY = []
    #print len(periods1), len(result1[stockIndex])
    for dateIndex in range(0, len(periods1)) :
    #for dateIndex in range(0, len(result1[0])) :
        #print assets[stockIndex].getAssetName(), stockIndex, dateIndex 
        
        tmpValue = result1[stockIndex][dateIndex][0]
        value = 0 if tmpValue < 0 else 1
        #print tmpValue , value
        tmpY.append(value)
    y.append(tmpY)

################################Test Set X##################################
#PERIOD
asOfDate = Date("20150617")
calendar = SouthKoreaCalendar(1)
pp = Period(asOfDate, calendar)
periods2 = pp.getPeriodByVertex(Vertex.valueOf("M1"))
#for x in periods2 :
#    print x
    
#DATA
dataClass = AbstractData(assets, dats, dataTypes, dataCondiTypes, dataConditions)
result2 = dataClass.getResult(calendar, periods2)

testX = []
for stockIndex in range(0, len(result2)) :
    tmpX = []
    for dateIndex in range(0, len(result2[0])) :
        tmpX.append(result2[stockIndex][dateIndex])
    testX.append(tmpX)
################################TEST SET Y #####################################
#PERIOD
asOfDate = asOfDate.plusDays(7)
calendar = SouthKoreaCalendar(1)
pp = Period(asOfDate, calendar)
periods3 = pp.getPeriodByNumber(len(periods2))

#for x in periods1 :
#    print x

dats1 = [TrainingDataType.DataEnum.ClosePrice,]
dataTypes1 = [TrainingDataType.TypeEnum.RateOfChange,]
dataCondiTypes1 = [TrainingDataType.ConditionEnum.NONE,]
dataConditions1 = [-7,]

dataClass1 = AbstractData(assets, dats1, dataTypes1, dataCondiTypes1, dataConditions1)
result3 = dataClass1.getResult(calendar, periods3)

testY = []
for stockIndex in range(0, len(result3)) :
    tmpY = []
    for dateIndex in range(0, len(periods3)) :
    #for dateIndex in range(0, len(result1[0])) :
        tmpValue = result3[stockIndex][dateIndex][0]
        value = 0 if tmpValue < 0 else 1
        #print tmpValue , value
        tmpY.append(value)
    testY.append(tmpY)

######################################ML #####################################
for index in range(0, len(assets)) :
    
    #print assets[index].getAssetName(),assets[index].getAssetCode()
    #print testY[index]
    scaledX = Normalizer().fit_transform(X[index])
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

