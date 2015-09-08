'''
Created on 2015. 9. 7.

@author: Jay
'''
from engine.portfolio.SelectAssets import SelectAsset
from abc import ABCMeta, abstractmethod
from util.DB.dbConnector import dbConnector
from util.DB.sqlMap import sqlMap
from engine.type.IndicatorType import IndicatorType

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
    
    