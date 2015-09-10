'''
Created on 2015. 9. 8.

@author: Jay
'''
from engine.procedure.AbstractIndicator import AbstractIndicator
from engine.type.TrainingDataType import TrainingDataType
from engine.data.TrainingData import TrainingData
import numpy as np
from util.DB.stringController import stringController as SC

class Indicator_MA(AbstractIndicator):
    '''
    http://www.ta-guru.com/Book/TechnicalAnalysis/TechnicalIndicators/MovingAverage.php5
    '''

    def setData(self):
        #DATA
        datasForX = [TrainingDataType.DataEnum.ClosePrice,]
        dataTypesForX = [TrainingDataType.TypeEnum.Value,]
        dataCondiTypesForX = [TrainingDataType.ConditionEnum.NONE,]
        dataConditionsForX = [0,]
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
        for stockIndex in range(0, len(self._value)):            
            result.append(self.calculate(stockIndex))            
        return result    
        
    def insertResult(self): 
        codeStr = SC.makeQuotation(self._indiType)
        period = self.getPeriod()
        for stockIndex in range(0, len(self._value)):
            totalQuery = "\
                INSERT INTO\
                    INDICATOR_DATA\
                    (`date`, `code`, `underlyingCode`, `value`, `CREATED_AT`, `UPDATED_AT`)\
                VALUES "
            
            result = self.calculate(stockIndex)
            assetStr = SC.makeQuotation(self._assets[stockIndex].getAssetCode())
            for timeIndex in range(0, len(period)) :
                dateStr = SC.makeQuotation(period[timeIndex].getDate())
                valueStr = SC.makeQuotation(repr(result[timeIndex]))
                query = dateStr + ", " + codeStr + ", " + assetStr + ", " + valueStr + ", now(), now()"
                #print period[timeIndex], result[timeIndex]
                #print query
                totalQuery = totalQuery + SC.makeParentheses(query) + ", "
                             
            resultQuery = totalQuery[:-2] + " ON DUPLICATE KEY UPDATE `value` = VALUES(VALUE) , `UPDATED_AT` = NOW()"
                    
            print resultQuery
            #print assetStr
            self.DB.insert(resultQuery)
                    
    def calculate(self, params):
        if self._type == "MASi" :
            return self.sma(self._value[params], self._window)
        elif self._type == "MAW" :
            return self.wma(self._value[params], self._window)
        elif self._type == "MAEW" :
            return self.ema(self._value[params], self._window)
        else :
            raise ValueError("Indicator type is improper")
    