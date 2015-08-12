'''
Created on 2015. 8. 12.

@author: Jay
'''

class dataEnums():
    
    class DataEnum(enumerate):
        ClosePrice = "CurrentPrice"
        TradingVolume = "TradingVolume"
        TradingSum = "TradingSum"
        OpenPrice = "OpenPrice"
        
    class TypeEnum(enumerate):
        Value = "Value"
        ChangeAmount = "ChangeAmount"
        RateOfChange = "RateOfChange"
    
    class ConditionEnum(enumerate):
        NONE = "NONE"
        LAG = "LAG"
    
    tableMap = {
        DataEnum.ClosePrice : "STOCK_SISAE",
        DataEnum.TradingVolume : "STOCK_SISAE",
        DataEnum.TradingSum : "STOCK_SISAE",
        DataEnum.OpenPrice : "STOCK_SISAE",
    }
    