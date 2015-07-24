#-*- coding: utf-8 -*-
'''
Created on 2015. 6. 18.

@author: Jay
'''
from util.sqlMap import sqlMap
from util.dbConnector import dbConnector
from util.stringController import stringController as SC

class HistoricalData():
    
    def __init__(self):
        '''
        Constructor
        '''
        self.dbInstance = dbConnector(sqlMap.connectInfo)
    
    #[asset][date]
    def getStockPrices(self, assetLists, periods):
        
        lenAssetList = len(assetLists)
        lenPeriods = len(periods)
        
        stockPrices = []
        #Make Time Statement
        timeStatement = ""            
        for timeIndex in range(0, lenPeriods):
            date = periods[timeIndex]                   
            timeStatement = timeStatement + date + SC.comma()
        timeStatement = SC.makeQuotation(timeStatement[:-1])
        #print timeStatement
        
        #Make Asset Statement
        assetStatement = ""        
        for assetIndex in range(0, lenAssetList):        
            assetCode = assetLists[assetIndex].getAssetCode()
            assetStatement = assetStatement + assetCode + SC.comma()
        assetStatement = SC.makeQuotation(assetStatement[:-1])
        #print assetStatement
                
        #Make Total Statement
        tmpTotalStatement = SC.makeParentheses(timeStatement + SC.comma() + assetStatement)
        totalStatement = sqlMap.SELECTHISTORICALSTOCKPRICES2 %(tmpTotalStatement)
        #print totalStatement
        
        #Get Asset Prices
        prices = self.dbInstance.select(totalStatement)
        #print(prices)
        
        for index in range(0, len(prices), lenPeriods):
            priceList = []
            for periodIndex in range(0, lenPeriods):                
                resultCode = prices[index + periodIndex][0]
                resultDate = prices[index + periodIndex][1]
                resultPrice = prices[index + periodIndex][2]                            
                #print(resultCode, resultDate, resultPrice)
                
                priceList.append(resultPrice)
                
            stockPrices.append(priceList)
            
        return stockPrices
            
    def getStockSisaeData(self, assetLists, periods):
        lenAssetList = len(assetLists)
        lenPeriods = len(periods)
        
        stockPrices = []
        #Make Time Statement
        timeStatement = ""            
        for timeIndex in range(0, lenPeriods):
            date = periods[timeIndex]                   
            timeStatement = timeStatement + date + SC.comma()
        timeStatement = SC.makeQuotation(timeStatement[:-1])
        #print timeStatement
        
        #Make Asset Statement
        assetStatement = ""        
        for assetIndex in range(0, lenAssetList):        
            assetCode = assetLists[assetIndex].getAssetCode()
            assetStatement = assetStatement + assetCode + SC.comma()
        assetStatement = SC.makeQuotation(assetStatement[:-1])
        #print assetStatement
                
        #Make Total Statement
        tmpTotalStatement = SC.makeParentheses(timeStatement + SC.comma() + assetStatement)
        totalStatement = sqlMap.SELECTHISTSTOCKSISAE %(tmpTotalStatement)
        #print totalStatement
        
        #Get Asset Prices
        prices = self.dbInstance.select(totalStatement)
        #print(prices)
        
        for index in range(0, len(prices), lenPeriods):
            priceList = []
            for periodIndex in range(0, lenPeriods):                
                resultCode = prices[index + periodIndex][0]
                resultDate = prices[index + periodIndex][1]
                resultPrice = prices[index + periodIndex][2:]                            
                #print(resultCode, resultDate, resultPrice)
                resultSisae = []
                for tmpX in resultPrice:
                    resultSisae.append(tmpX)
                priceList.append(resultSisae)
                
            stockPrices.append(priceList)
            
        return stockPrices
        