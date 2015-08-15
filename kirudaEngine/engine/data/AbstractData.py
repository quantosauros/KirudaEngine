'''
Created on 2015. 8. 12.

@author: Jay
'''
from engine.data.UnitData import UnitData
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
                
                
                #===================================================================
                # if dataType is dataEnums.TypeEnum.Value :
                #     print "A"
                #     #tmp = UnitData(data, date, self.Assets)
                #     #tmp.getResult()
                #     
                # elif dataType is dataEnums.TypeEnum.ChangeAmount : 
                #     print "B"            
                #     #tmp1 = UnitData(data, date, self.Assets)
                #     #tmp1.getResult()
                #     #tmp2 = UnitData(data, date.plusDays(condition), self.Assets)
                #     #tmp2.getResult()
                #     
                # elif dataType is dataEnums.TypeEnum.RateOfChange :
                #     print "C"
                #     #tmp = UnitData(data, date, self.Assets)
                #     #tmp.getResult()
                #===================================================================
                tmpResult.append(self.DB.select(query))
            
            results.append(tmpResult)
        #print tableNames + "; " + columnNames
        return results
    
    def getResult2(self, date):
        tableNames = ""
        columnNames = ""
        curDates = ""
        lagDates = ""
        for index in range(0, self.numOfData):
            data = self.data[index]
            dataType = self.dataType[index]
            condiType = self.condiType[index]
            condition = self.condition[index]
                        
            tableName = dataEnums.tableMap[data]
            columnName = data
            curDate = date.getDate()
            lagDate = date.plusDays(condition).getDate()
            
            tableNames = tableNames + tableName + ";"
            columnNames = columnNames + columnName + ";"
            curDates = curDates + curDate + ";"
            lagDates = lagDates + lagDate + ";"
            
        code = QueryMaker.stockCodeQueryMaker(self.Assets, '0')
            
        return tableNames + ", " + columnNames + ", " + curDates + ", " + lagDates
    
        