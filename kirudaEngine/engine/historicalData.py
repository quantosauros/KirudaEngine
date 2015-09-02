#-*- coding: utf-8 -*-
'''
Created on 2015. 6. 18.

@author: Jay
'''
from util.DB.sqlMap import sqlMap
from util.DB.dbConnector import dbConnector
from util.DB.stringController import stringController as SC
from util.DB.QueryMaker import QueryMaker

class HistoricalData():
    
    def __init__(self):
        self.dbInstance = dbConnector(sqlMap.connectInfo)
    
    def getStockPrices(self, assetLists, periods):
        '''
        [asset][date]
        execute CALL PC_SLT_HISTSTOCKPRICE to get historical close price of stocks.    
        '''    
        lenAssetList = len(assetLists)
        lenPeriods = len(periods)
        
        stockPrices = []
        #Make Time Statement
        timeStatement = QueryMaker.dateQueryMaker(periods, '1')        
        #print timeStatement
        
        #Make Asset Statement
        assetStatement = QueryMaker.stockCodeQueryMaker(assetLists, '1')
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
        '''
        execute CALL PC_SLT_HISTSTOCKSISAE to get stock_sisae data of stocks
        '''
        lenAssetList = len(assetLists)
        lenPeriods = len(periods)
        
        stockPrices = []
        #Make Time Statement
        timeStatement = QueryMaker.dateQueryMaker(periods, '1')
        #print timeStatement
        
        #Make Asset Statement        
        assetStatement = QueryMaker.stockCodeQueryMaker(assetLists, '1')
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
        