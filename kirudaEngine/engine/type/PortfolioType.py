'''
Created on 2015. 6. 18.

@author: Jay
'''

class PortfolioType():
    
    PER = 'PER'
    #KS, KQ
    MARKET = 'MARKET'
    MARKETCAP = 'MARKETCAP'
    CODE = 'CODE'
    DESIGNATED = 'DESIGNATED'
    
    tableMap = {
        "STOCK_INFO" : "B",
        "STOCK_SISAE" : "A",    
    }
    
    conditionTable = {
        MARKET : "STOCK_INFO",
        PER : "STOCK_SISAE",
        MARKETCAP : "STOCK_SISAE",
        CODE : "STOCK_SISAE",
        DESIGNATED : "STOCK_SISAE"
         
    }
    