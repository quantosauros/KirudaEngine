'''
Created on 2015. 8. 12.

@author: Jay
'''
from util.dataEnums import dataEnums
from util.QueryMaker import QueryMaker
from util.dbConnector import dbConnector
from util.sqlMap import sqlMap
from util.BusinessDayConvention import BusinessDayConvention

class AbstractData():
        
    def __init__(self, assets, data, dataType, condiType, condition = ""):
        self.data = data
        self.dataType = dataType
        self.condiType = condiType
        self.condition = condition
        self.Assets = assets
        self.numOfData = len(data)
        self.DB = dbConnector(sqlMap.connectInfo);
        
    def getResult(self, calendar, periods):
        '''
        Result : [date][data][stockCode][column]
        
        '''
        results = []
        for periodIndex in range(0, len(periods)):
            tmpResult = []
            date = periods[periodIndex]
            #tableNames = ""
            #columnNames = ""
            for index in range(0, self.numOfData):
                data = self.data[index]
                dataType = self.dataType[index]
                condiType = self.condiType[index]
                condition = self.condition[index]
                tableName = dataEnums.tableMap[data]
                #columnName = data
                #tableNames = tableNames + tableName
                #columnNames = columnNames + columnName
                currDate = date.getDate()
                tmpLagDate = date
                for index in range(0, abs(condition)):                    
                    tmpLagDate = calendar.adjustDate(tmpLagDate.plusDays(-1),
                                                     BusinessDayConvention.PRECEDING)
                lagDate = tmpLagDate.getDate()
                
                print currDate, lagDate
                                
                code = QueryMaker.stockCodeQueryMaker(self.Assets, '0')
                
                query = 'CALL PC_GETDATA("' + data + '", "' + tableName + '",' + \
                    '"' + currDate + '","' + lagDate + \
                    '", "' + code +'");'
                #print query
                        
                tmpResult.append(self.DB.select(query))
            
            results.append(tmpResult)
        #print tableNames + "; " + columnNames
        return results
    