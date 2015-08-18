'''
Created on 2015. 6. 18.

@author: Jay
'''

class assetConditions():
    
    PER = 'PER'
    #KS, KQ
    MARKET = 'MARKET'
    MARKETCAP = 'MARKETCAP'
    CODE = 'CODE'
    
    tableMap = {
        "stock_info" : "B",
        "stock_sisae" : "A",    
    }
    
    conditionTable = {
        MARKET : "stock_info",
        PER : "stock_sisae",
        MARKETCAP : "stock_sisae",
        CODE : "stock_sisae",
         
    }
    