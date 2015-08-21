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
        
        Result = [stockCode][Date][Data]
        
        '''
        #results = []
        resultArray = [[] for _ in range(len(self.Assets))]
        for stockIndex in range(len(self.Assets)):
            resultArray[stockIndex] = [[] for _ in range(len(periods))]
        
        #print len(resultArray), len(resultArray[0])
        
        for periodIndex in range(0, len(periods)):
            #tmpResult = []
            date = periods[periodIndex]
                       
            for dataIndex in range(0, self.numOfData):
                data = self.data[dataIndex]
                dataType = self.dataType[dataIndex]
                condiType = self.condiType[dataIndex]
                condition = self.condition[dataIndex]
                tableName = dataEnums.dataTableMap[data]

                currDate = date.getDate()                                
                #Calculate lagDate from calendar
                tmpLagDate = date
                for index in range(0, abs(condition)):                    
                    tmpLagDate = calendar.adjustDate(tmpLagDate.plusDays(-1),
                                                     BusinessDayConvention.PRECEDING)
                lagDate = tmpLagDate.getDate()
                
                #print currDate, lagDate
                
                #Make Query 
                code = QueryMaker.stockCodeQueryMaker(self.Assets, '0')                
                query = 'CALL PC_GETDATA("' + data + '", "' + tableName + '",' + \
                    '"' + currDate + '","' + lagDate + \
                    '", "' + code +'");'
                #print query
                
                #[stockCode][column]
                queryResult = self.DB.select(query)
                columnIndex = dataEnums.typeTableMap[dataType]
                
                for stockIndex in range(0, len(queryResult)):
                    resultArray[stockIndex][periodIndex].append(queryResult[stockIndex][columnIndex])
                    #print queryResult[stockIndex][0], queryResult[stockIndex][1], \
                    #    queryResult[stockIndex][2], queryResult[stockIndex][3],\
                    #    queryResult[stockIndex][columnIndex]
                    #print resultArray[stockIndex][periodIndex]
                    
                #tmpResult.append(queryResult[stockIndex][columnIndex])
            
            #results.append(tmpResult)
        #print tableNames + "; " + columnNames
        return resultArray
    