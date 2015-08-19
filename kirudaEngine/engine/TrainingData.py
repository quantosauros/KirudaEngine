'''
Created on 2015. 8. 19.

@author: jayjl
'''
from engine.data.AbstractData import AbstractData
from util.Period import Period
from util.dataEnums import dataEnums

class TrainingData():

    def __init__(self, assets, datas, dataTypes, dataConditionTypes, dataConditions):
        '''
        Constructor
        '''
        self.assets = assets
        #self.datas = datas;
        #self.dataTypes = dataTypes
        #self.dataConditionTypes = dataConditionTypes
        #self.dataConditions = dataConditions
        self.dataClass = AbstractData(assets, datas, dataTypes, dataConditionTypes, dataConditions)
                
    def getTrainingXData(self, asOfDate, calendar, vertex):
        #PERIOD
        pp = Period(asOfDate, calendar)
        periods = pp.getPeriodByVertex(vertex)
        print len(periods)
        result = self.dataClass.getResult(calendar, periods)
        X = []
        for stockIndex in range(0, len(result)) :
            tmpX = []
            for dateIndex in range(0, len(result[0])) :
                tmpX.append(result[stockIndex][dateIndex])
            X.append(tmpX)
        return X
    
    def getTrainingYData(self, asOfDate, calendar, lagTime, numOfPeriod):
        datas = [dataEnums.DataEnum.ClosePrice,]
        dataTypes = [dataEnums.TypeEnum.RateOfChange,]
        dataConditionTypes = [dataEnums.ConditionEnum.NONE,]
        dataConditions = [-lagTime,]
        
        pp = Period(asOfDate.plusDays(lagTime), calendar)
        periods = pp.getPeriodByNumber(numOfPeriod)
            
        dataClass = AbstractData(self.assets, datas, dataTypes, dataConditionTypes, dataConditions)
                
        result = dataClass.getResult(calendar, periods)
        
        y = []
        for stockIndex in range(0, len(result)) :
            tmpY = []
            for dateIndex in range(0, len(result[0])) :
            #for dateIndex in range(0, len(result1[0])) :
                #print self.assets[stockIndex].getAssetName(), stockIndex, dateIndex 
                
                tmpValue = result[stockIndex][dateIndex][0]
                value = 0 if tmpValue < 0 else 1
                #print tmpValue , value
                tmpY.append(value)
            y.append(tmpY)
            
        return y
        