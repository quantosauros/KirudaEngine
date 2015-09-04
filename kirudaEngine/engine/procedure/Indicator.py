'''
Created on 2015. 9. 3.

@author: Jay
'''
from engine.type.IndicatorType import IndicatorType
from util.DB.dbConnector import dbConnector
from util.DB.sqlMap import sqlMap

class Indicator():
    
    def __init__(self, calendar, indicatorType):
        
        self._calendar = calendar
        self._indicatorType = indicatorType
        self.DB = dbConnector(sqlMap.connectInfo);
        
    def generate(self, date):
        tmp = IndicatorType.dataTableMap[self._indicatorType]
        type = tmp[:-3]
        numOfTermDate = int(tmp[-3:]) 
        #print type
        #print numOfTermDate
        
        prevDate = self._calendar.getBusinessDayFromDate(date, -1)
        dropDate = self._calendar.getBusinessDayFromDate(date, -numOfTermDate)        
        #print date, prevDate, dropDate
        
        query = "CALL PC_INST_INDICATOR_MA('" + str(date) + "', '" + str(prevDate) +\
                "', '" + str(dropDate) + "', '" + repr(numOfTermDate) + "', '" + type + "');"
        print query
        
        self.DB.insert(query)
        
                
        