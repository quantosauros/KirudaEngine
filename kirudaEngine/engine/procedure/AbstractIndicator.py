'''
Created on 2015. 9. 7.

@author: Jay
'''
from engine.portfolio.SelectAssets import SelectAsset
from abc import ABCMeta, abstractmethod
from util.DB.dbConnector import dbConnector
from util.DB.sqlMap import sqlMap
from engine.type.IndicatorType import IndicatorType
import numpy as np

class AbstractIndicator():
    __metaclass__ = ABCMeta
    
    def __init__(self, calendar, asOfDate, vertex, indicatorType):
        self._calendar = calendar
        self._asOfDate = asOfDate
        self._vertex = vertex
        self._DB = dbConnector(sqlMap.connectInfo);
        self._indicatorType = indicatorType;
        self.setAsset()
        self.setData()
        self.setIndicatorType()
        
    def setAsset(self):
        #ASSETS
        sa = SelectAsset()
        #self._assets = sa.select([], [], self._asOfDate)
        self._assets = sa.selectTest()
        
    def setIndicatorType(self):
        self._indiType = IndicatorType.dataTableMap[self._indicatorType]
        self._type = self._indiType[:-3]
        self._window = int(self._indiType[-3:]) 
    
    @abstractmethod
    def setData(self): pass
    
    @abstractmethod
    def getResult(self): pass
    
    @abstractmethod
    def insertResult(self): pass        
    
    @abstractmethod
    def calculate(self, params): pass    
    
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
            