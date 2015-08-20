'''
Created on 2015. 8. 19.

@author: jayjl
'''
from engine.data.AbstractData import AbstractData
from util.Period import Period
from util.dataEnums import dataEnums
from util.Vertex import Vertex

class TrainingData():

    def __init__(self, assets, calendar, datas, dataTypes, dataConditionTypes, dataConditions):
        
        self.assets = assets
        self.calendar = calendar
        self.dataClassForX = AbstractData(assets, datas, dataTypes, dataConditionTypes, dataConditions)
                
    def genTrainingXData(self, asOfDate, vertex):
        #PERIOD
        pp = Period(asOfDate, self.calendar)
        periods = pp.getPeriodByVertex(vertex)
        #print len(periods)
        result = self.dataClassForX.getResult(self.calendar, periods)
        X = []
        for stockIndex in range(0, len(result)) :
            tmpX = []
            for dateIndex in range(0, len(result[0])) :
                tmpX.append(result[stockIndex][dateIndex])
            X.append(tmpX)
            
        self.asOfDate = asOfDate
        self.X = X
        self.numOfPeriod = len(periods)
        
    def genTrainingYData(self, asOfDate, lagTime, numOfPeriod):
        datas = [dataEnums.DataEnum.ClosePrice,]
        dataTypes = [dataEnums.TypeEnum.RateOfChange,]
        dataConditionTypes = [dataEnums.ConditionEnum.NONE,]
        dataConditions = [-lagTime,]
        
        pp = Period(asOfDate.plusDays(lagTime), self.calendar)
        periods = pp.getPeriodByNumber(numOfPeriod)

        self.dataClassForY = AbstractData(self.assets, datas, dataTypes, 
                                 dataConditionTypes, dataConditions)
                
        result = self.dataClassForY.getResult(self.calendar, periods)
        
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
            
        self.lagTime = lagTime
        self.y = y
    
    def getX(self):
        return self.X
    
    def getY(self):
        return self.y
    
    def getNumOfPeriod(self):
        return self.numOfPeriod
    
    def genNextX(self, date):
        for stockIndex in range(0, len(self.X)) :
            self.X[stockIndex].pop(0)
            
        #PERIOD
        pp = Period(date, self.calendar)
        periods = pp.getPeriodByVertex(Vertex.valueOf("D0"))
        
        tmpResult = self.dataClassForX.getResult(self.calendar, periods)
        for stockIndex in range(0, len(self.X)) :
            for dateIndex in range(0, len(tmpResult[stockIndex])) :
                self.X[stockIndex].append(tmpResult[stockIndex][dateIndex])        
        
        return self.X
        
    def genNextY(self, date):
        for stockIndex in range(0, len(self.y)) :
            self.y[stockIndex].pop(0)
        
        #PERIOD
        pp = Period(date, self.calendar)
        periods = pp.getPeriodByVertex(Vertex.valueOf("D0"))
        
        tmpResult = self.dataClassForY.getResult(self.calendar, periods)

        for stockIndex in range(0, len(self.y)) :
            for dateIndex in range(0, len(tmpResult[stockIndex])) :
                tmpValue =tmpResult[stockIndex][dateIndex][0]
                value = 0 if tmpValue < 0 else 1
                
                self.y[stockIndex].append(value)        
        
        return self.y
    