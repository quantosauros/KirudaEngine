'''
Created on 2015. 9. 8.

@author: Jay
'''
from engine.procedure.AbstractIndicator import AbstractIndicator
from engine.type.TrainingDataType import TrainingDataType
from engine.data.TrainingData import TrainingData
import numpy as np

class Indicator_Volatility(AbstractIndicator):
    '''
    http://www.ta-guru.com/Book/TechnicalAnalysis/TechnicalIndicators/Volatility.php5
    '''
    
    def setData(self):
        #DATA
        datasForX = [
                     TrainingDataType.DataEnum.ClosePrice,                     
                    ]
        dataTypesForX = [
                         TrainingDataType.TypeEnum.Value,
                         ]
        dataCondiTypesForX = [
                              TrainingDataType.ConditionEnum.NONE,
                              ]
        dataConditionsForX = [
                              0,                              
                              ]
        tData = TrainingData(self._assets, self._calendar, 
                             datasForX, dataTypesForX, dataCondiTypesForX, 
                             dataConditionsForX)
        tData.genTrainingXData(self._asOfDate, self._vertex)
        X = tData.getX()
        self._period = tData.getPeriodX()
        self._value = []
        for i in range(0, len(X)):
            newX = []
            for j in range(0, len(X[0])):
                newX.append(X[i][j][0])
            self._value.append(newX)
            
            
    def getResult(self):
        result = []
        for index in range(0, len(self._value)):            
            result.append(self.calculate(self._value[index]));
            
        return result
    
    def insertResult(self):
        #TO BE IMPLEMENTED
        print "TO BE IMPLEMENTED"
        
    def calculate(self, params):
        return self.calcSMV(params)
        
    def calcSMV(self, params):
        #params : closePrices, window
        closePrices = params
        sma = self.sma(closePrices, self._window)
        totalNum = len(closePrices) - self._window + 1
        
        SMV = np.zeros(totalNum)
        Vol = np.zeros(totalNum)
        for windowIndex in range(0, totalNum) :
            tmp = 0
            for index in range(windowIndex, windowIndex + self._window) :
                tmpValue = (closePrices[index] - sma[windowIndex])
                tmp = tmp + tmpValue * tmpValue
            SMV[windowIndex] = tmp / self._window
            Vol[windowIndex] = np.sqrt(SMV[windowIndex]) / SMV[windowIndex]
        
        return Vol
        
        
        
            