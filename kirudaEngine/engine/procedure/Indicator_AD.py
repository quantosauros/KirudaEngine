'''
Created on 2015. 9. 7.

@author: Jay
'''
from engine.procedure.AbstractIndicator import AbstractIndicator
from engine.type.TrainingDataType import TrainingDataType
from engine.data.TrainingData import TrainingData
import numpy as np

class Indicator_AD(AbstractIndicator):
    '''
    http://www.ta-guru.com/Book/TechnicalAnalysis/TechnicalIndicators/AccumulationDistribution.php5
    '''
    def setData(self):
        #DATA
        datasForX = [
                     TrainingDataType.DataEnum.ClosePrice, 
                     TrainingDataType.DataEnum.LowestPrice,
                     TrainingDataType.DataEnum.HighestPrice,
                     TrainingDataType.DataEnum.TradingVolume,
                    ]
        dataTypesForX = [
                         TrainingDataType.TypeEnum.Value,
                         TrainingDataType.TypeEnum.Value,
                         TrainingDataType.TypeEnum.Value,
                         TrainingDataType.TypeEnum.Value,
                         ]
        dataCondiTypesForX = [
                              TrainingDataType.ConditionEnum.NONE,
                              TrainingDataType.ConditionEnum.NONE,
                              TrainingDataType.ConditionEnum.NONE,
                              TrainingDataType.ConditionEnum.NONE,
                              ]
        dataConditionsForX = [
                              0,0,0,0,                              
                              ]
        tData = TrainingData(self._assets, self._calendar, 
                             datasForX, dataTypesForX, dataCondiTypesForX, 
                             dataConditionsForX)
        tData.genTrainingXData(self._asOfDate, self._vertex)
        X = tData.getX()
        self._period = tData.getPeriodX()
        self._value = [[] for _ in range(len(datasForX))]
        for i in range(0, len(X)):
            newX1 = []
            newX2 = []
            newX3 = []
            newX4 = []
            for j in range(0, len(X[0])):
                newX1.append(X[i][j][0])
                newX2.append(X[i][j][1])
                newX3.append(X[i][j][2])
                newX4.append(X[i][j][3])                
            self._value[0].append(newX1)
            self._value[1].append(newX2)
            self._value[2].append(newX3)
            self._value[3].append(newX4)
                
    def getResult(self):
        result = []
        for index in range(0, len(self._value)):
            result.append(self.calculate(self._value[0][index], self._value[1][index], 
                                         self._value[2][index], self._value[3][index]));
            
        return result
    
    def insertResult(self):
        #TO BE IMPLEMENTED
        print "TO BE IMPLEMENTED"
    
    def calculate(self, closePrices, lowestPrices, highestPrices, volumes):
        totalNum = len(closePrices)
        AD = np.zeros(totalNum)
        for index in range(0, totalNum):
            cPrice = float(closePrices[index])
            lPrice = float(lowestPrices[index])
            hPrice = float(highestPrices[index])
            CLV = (cPrice - lPrice - hPrice + cPrice) / (hPrice - lPrice)            
            prevAD = 0.0 if index == 0 else AD[index - 1]
            AD[index] = CLV * float(volumes[index]) + prevAD
        
        return AD
