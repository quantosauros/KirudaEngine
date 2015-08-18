'''
Created on 2015. 8. 12.

@author: Jay
'''
from util.dataEnums import dataEnums
from util.QueryMaker import QueryMaker
from util.dbConnector import dbConnector
from util.sqlMap import sqlMap

class AbstractData():
        
    def __init__(self, assets, data, dataType, condiType, condition = ""):
        self.data = data
        self.dataType = dataType
        self.condiType = condiType
        self.condition = condition
        self.Assets = assets
        self.numOfData = len(data)
        self.DB = dbConnector(sqlMap.connectInfo);
        
    def getResult(self, periods):
        
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
                
                code = QueryMaker.stockCodeQueryMaker(self.Assets, '0')
                
                query = 'CALL PC_TEST3("' + data + '", "' + tableName + '",' + \
                    '"' + date.getDate() + '","' + date.plusDays(condition).getDate() + \
                    '", "' + code +'");'
                #print query
                        
                tmpResult.append(self.DB.select(query))
            
            results.append(tmpResult)
        #print tableNames + "; " + columnNames
        return results
    