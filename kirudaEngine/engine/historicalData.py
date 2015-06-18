#-*- coding: utf-8 -*-
'''
Created on 2015. 6. 18.

@author: Jay
'''
from util.sqlMap import sqlMap
from util.dbConnector import dbConnector

class HistoricalData():
    
    def __init__(self):
        '''
        Constructor
        '''
        self.dbInstance = dbConnector(sqlMap.connectInfo)
        
    #[asset][date]
    def getStockPrices(self, assetLists, periods):
        
        stockPrices = []
        for assetIndex in range(0, len(assetLists)):        
            assetCode = assetLists[assetIndex].getAssetCode()
            priceList = []            
            timeStatement = ""
            for timeIndex in range(0, len(periods)):
                date = periods[timeIndex]   
                tmp = " DATE = '" + date + "' OR"                 
                timeStatement = timeStatement + tmp
                        
            totalStatement = sqlMap.SELECTHISTORICALSTOCKPRICES %(assetCode, timeStatement[:-2])
            #print(totalStatement)
            prices = self.dbInstance.select(totalStatement)
            #print(prices)
            
            # TODO: 해당날짜에 가격이 없을 경우 예외처리
            for timeIndex in range(0, len(periods)):
                #print(assetCode)
                if periods[timeIndex] == prices[timeIndex][0]:
                    priceList.append(prices[timeIndex][1])
                else :
                    priceList.append(0)
                        
            stockPrices.append(priceList)            
            
        return stockPrices
        
        