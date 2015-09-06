'''
Created on 2015. 9. 3.

@author: Jay
'''
from engine.type.IndicatorType import IndicatorType
from util.DB.dbConnector import dbConnector
from util.DB.sqlMap import sqlMap
import numpy as np
from engine.type.TrainingDataType import TrainingDataType
from engine.data.TrainingData import TrainingData
from engine.portfolio.SelectAssets import SelectAsset
from util.DB.stringController import stringController as SC

class Indicator():
    
    def __init__(self, asOfDate, vertex, calendar, indicatorType):
        self._asOfDate = asOfDate
        self._vertex = vertex
        
        #ASSETS
        sa = SelectAsset()
        self._assets = sa.select([], [], asOfDate)
        #self._assets = sa.selectTest()
        
        #DATA
        datasForX = [TrainingDataType.DataEnum.ClosePrice,]
        dataTypesForX = [TrainingDataType.TypeEnum.Value,]
        dataCondiTypesForX = [TrainingDataType.ConditionEnum.NONE,]
        dataConditionsForX = [0,]
        tData = TrainingData(self._assets, calendar, datasForX, dataTypesForX, dataCondiTypesForX, dataConditionsForX)
        tData.genTrainingXData(asOfDate, vertex)
        X = tData.getX()
        self._period = tData.getPeriodX()
        self._value = []
        for i in range(0, len(X)):
            newX = []
            for j in range(0, len(X[0])):
                newX.append(X[i][j][0])
            self._value.append(newX)
            
        self._indiType = IndicatorType.dataTableMap[indicatorType]
        self._type = self._indiType[:-3]
        self._window = int(self._indiType[-3:]) 
        
        self.DB = dbConnector(sqlMap.connectInfo);
        
    def generate(self):
        self._result = []
        if self._type == "MASi" :
            for index in range(0, len(self._value)):
                self._result.append(self.sma(self._value[index], self._window))
        elif self._type == "MAW" :
            for index in range(0, len(self._value)):
                self._result.append(self.wma(self._value[index], self._window))
        elif self._type == "MAEW" :
            for index in range(0, len(self._value)):
                self._result.append(self.ema(self._value[index], self._window))
        else :
            raise ValueError("Indicator type is improper")

    def getResult(self):
        return self._result
    
    def insertResult(self):
        codeStr = SC.makeQuotation(self._indiType)
        period = self.getPeriod()
        totalQuery = "\
                INSERT INTO\
                    INDICATOR_DATA\
                    (`date`, `code`, `underlyingCode`, `value`, `CREATED_AT`, `UPDATED_AT`)\
                VALUES "
        for stockIndex in range(0, len(self._result)) :
            
            
            #print assets[stockIndex].getAssetCode()
            assetStr = SC.makeQuotation(self._assets[stockIndex].getAssetCode())
            for timeIndex in range(0, len(period)) :
                dateStr = SC.makeQuotation(period[timeIndex].getDate())
                valueStr = SC.makeQuotation(repr(self._result[stockIndex][timeIndex]))
                query = dateStr + ", " + codeStr + ", " + assetStr + ", " + valueStr + ", now(), now()"
                #print period[timeIndex], result[stockIndex][timeIndex]
                #print query
                totalQuery = totalQuery + SC.makeParentheses(query) + ", "
            
             
            resultQuery = totalQuery[:-2] + " ON DUPLICATE KEY UPDATE `value` = VALUES(VALUE) , `UPDATED_AT` = NOW()"
                    
            print resultQuery  
            self.DB.insert(resultQuery)
        
    def getAssetList(self):
        return self._assets
    
    def getPeriod(self):
        return self._period[self._window - 1:]
    
    def sma(self, values, window):
        if (len(values) < window) :
            raise ValueError("data is too short")
        weights = np.repeat(1.0, window)/window
        #print weights
        sma = np.convolve(values, weights, 'valid')
        return sma
    
    def wma(self, values, window):
        if len(values) < window :
            raise ValueError("data is too short")
        sum = window * (window + 1.0) / 2.0
        weights = np.arange(1, window + 1, dtype=np.float) / sum
        totalNum = len(values) - window + 1
        wma = np.zeros(totalNum)
        for i in range(0, window) :
            wma[0] = wma[0] + values[i] * weights[i]
        
        for j in range(1, totalNum) :
            lastIndex = j - 1 + window
            tmp = np.sum(values[j-1: lastIndex]) - values[lastIndex] * window
            #print j, wma[j-1], np.sum(values[j-1: lastIndex]), values[lastIndex], tmp, tmp / sum 
            wma[j] = wma[j-1] - tmp / sum
        return wma
  
    
    def ema(self, values, window):
        """
        Calculates Exponential Moving Average
        http://fxtrade.oanda.com/learn/forex-indicators/exponential-moving-average
        """
        if len(values) < 2 + window:
            raise ValueError("data is too short")
        totalNum = len(values) - window + 1
        ema = np.zeros(totalNum)
        c = 2.0 / (window + 1.0)
        ema[0] = self.sma(values[-window*2-1 : -window-1], window)
        index = 1
        for value in values[-window - 1:]:
            ema[index] = (c * value) + ((1 - c) * ema[index - 1])
            index = index + 1
        return ema
    
    #===========================================================================
    # def __init__(self, calendar, indicatorType):
    #     
    #     self._calendar = calendar
    #     self._indicatorType = indicatorType
    #     self.DB = dbConnector(sqlMap.connectInfo);
    #     
    #         
    # def generate(self, date):
    #     tmp = IndicatorType.dataTableMap[self._indicatorType]
    #     type = tmp[:-3]
    #     numOfTermDate = int(tmp[-3:]) 
    #     #print type
    #     #print numOfTermDate
    #     
    #     prevDate = self._calendar.getBusinessDayFromDate(date, -1)
    #     dropDate = self._calendar.getBusinessDayFromDate(date, -numOfTermDate)        
    #     #print date, prevDate, dropDate
    #     
    #     query = "CALL PC_INST_INDICATOR_MA('" + str(date) + "', '" + str(prevDate) +\
    #             "', '" + str(dropDate) + "', '" + repr(numOfTermDate) + "', '" + type + "');"
    #     print query
    #     
    #     self.DB.insert(query)
    #     
    #             
    #===========================================================================
    