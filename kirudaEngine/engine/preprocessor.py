'''
Created on 2015. 7. 22.

@author: thCho
'''

from datetime import date
import datetime
import math

from util.dbConnector import dbConnector
from util.sqlMap import sqlMap
from util.stringController import stringController as SC
from engine.selectAssets import SelectAsset
from util.assetConditions import assetConditions

class preprocessor:
    def __init__(self):
#     def __init__(self, returnTable, returnColumn):
#         self.returnTable = returnTable
#         self.returnColumn = returnColumn
        self.dbInstance = dbConnector(sqlMap.connectInfo)
        self.sa = SelectAsset()
        self.variables = [assetConditions.MARKET]
        self.conditions = ["='KQ'"]
        #variables = [assetConditions.CODE]
        #conditions = [" in ('KS005930', 'KS008770')"]
        #variables = [assetConditions.MARKET, assetConditions.PER]
        #conditions = ["='KQ'", ">'9'"]
        self.assets = self.sa.select(self.variables, self.conditions)
#     table type: single array
#     tableColumn type: dual array: [table name][columns] : column Names
    def getXtable_train(self, Xtable, tableColumn, period, timeLag, conditionCommand):
        tableLength = len(Xtable)
        table = []
        
        stockCodeList = []
        stockCodeList = self.assets
        
        for stock in range(0, len(stockCodeList)):
            stockCode = stockCodeList[stock].assetCode
            tmpTimeStatement = "SELECT DISTINCT(date) FROM STOCK_SISAE WHERE CODE = '"+stockCode+"' AND " + period[0] + " <= date  AND date <= " + period[1] 
            tmpTimePeriod = self.dbInstance.select(tmpTimeStatement)
            timeNum = len(tmpTimePeriod)
            trainingSet = []  
            tmpTrainingData = []  
            for i in range(0, len(Xtable)):
                
                columns = tableColumn[i]
                columnStatement ='date,' + columns[0] + ','
                for j in range(1, len(columns)):
                    if j != len(columns) - 1 :
                        columnStatement += (columns[j] + ',')
                    else:
                        columnStatement += (columns[j])
                if conditionCommand[i] == '':
                    nullString = "Code='" + stockCode + "'"
                    tmpTrainingStatement =sqlMap.SELECTTRAININGDATA %(columnStatement, Xtable[i], period[0], period[1], stockCode, nullString)
                else:
                    tmpTrainingStatement =sqlMap.SELECTTRAININGDATA %(columnStatement, Xtable[i], period[0], period[1], stockCode, conditionCommand[i] )
                tmpTableSet = self.dbInstance.select(tmpTrainingStatement)
                tmpTableSetList = list(tmpTableSet)
                if len(tmpTrainingData) == 0:
                    tmpTrainingData = list(tmpTableSet)
                else:
                    for timeIndex in range(0, timeNum):
                        tmpTrainingData[timeIndex] = (tmpTrainingData[timeIndex] + tmpTableSet[timeIndex])
                        print(timeIndex)
#                         for dataIndex in range(0, len(tmpTableSet[timeIndex])):
#                             tmpTrainingData[timeIndex]+=tmpTableSet[timeIndex][dataIndex]
                        
            
        
            trainingSet.append(tmpTrainingData)    
            
        return 0
    
    def getYColumn_train(self):
        return 0
    
    def getXtable_test(self, Xtable, period, timeLag):
        tableLength = len(Xtable)
        return 0
    
    def getYColumn_test(self):
        return 0
    
        
def demo():
    dd = preprocessor()
    c = dd.getXtable_train(['stock_sisae', 'stock_trader'],[['currentPrice', 'netChange', 'tradingVolume', 'EPS', 'PER', 'foreignHoldingStock', 'shortVolume'],['sellVolume', 'buyVolume', 'sellAmount', 'buyAmount']],['20150202','20150505'], 0.25,['','traderCode = "F001"'])


if __name__ == '__main__':
    demo()   
#     print(d2)