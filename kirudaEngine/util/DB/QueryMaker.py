'''
Created on 2015. 8. 12.

@author: Jay
'''
from util.DB.stringController import stringController as SC

class QueryMaker():
    
    '''
    make query statement of dates from date array
    example : periods = ['20150611','20150612','20150615','20150616','20150617','20150618']
    result : 
        type 0 : '20150611','20150612','20150615','20150616','20150617','20150618'
        type 1 : '20150611,20150612,20150615,20150616,20150617,20150618'
    '''
    @staticmethod
    def dateQueryMaker(dates, type = '0'):
        lenDates = len(dates)
        timeStatement = ""            
        for timeIndex in range(0, lenDates):
            date = dates[timeIndex]            
            if type is '0':
                date = SC.makeQuotation(date)
                                                       
            timeStatement = timeStatement + date + SC.comma()
        if type is '0' :
            return timeStatement[:-1]
        elif type is '1' : 
            return SC.makeQuotation(timeStatement[:-1])
    
    '''
    make query statement of stock codes from assetlists built by "class Asset()"
    result : 
        type 0 : 'KQ000250','KQ000440','KQ001000','KQ001540'
        type 1 : 'KQ000250,KQ000440,KQ001000,KQ001540'
    '''
    @staticmethod
    def stockCodeQueryMaker(assetLists, type = '0'):
        lenAssetLists = len(assetLists)
        assetStatement = ""        
        for assetIndex in range(0, lenAssetLists):        
            assetCode = assetLists[assetIndex].getAssetCode()
            if type is '0':
                assetCode = SC.makeQuotation(assetCode)
                
            assetStatement = assetStatement + assetCode + SC.comma()
        if type is '0' :
            return assetStatement[:-1]
        elif type is '1' : 
            return SC.makeQuotation(assetStatement[:-1])       
    
    
    