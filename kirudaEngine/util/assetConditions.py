'''
Created on 2015. 6. 18.

@author: Jay
'''

class assetConditions():
    
    PER = 'PER'
    #KS, KQ
    MARKET = 'MARKET'
    MARKETCAP = 'MARKETCAP'
    
    tableMap = {
        "STOCK_INFO" : "B",
        "STOCK_SISAE" : "A",    
    }
    
    conditionTable = {
        MARKET : "STOCK_INFO",
        PER : "STOCK_SISAE",
        MARKETCAP : "STOCK_SISAE",
         
    }
    