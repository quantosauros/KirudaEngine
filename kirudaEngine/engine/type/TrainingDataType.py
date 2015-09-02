'''
Created on 2015. 8. 12.

@author: Jay
'''

class TrainingDataType():
    
    class DataEnum(enumerate):
        ClosePrice = "CurrentPrice"
        TradingVolume = "TradingVolume"
        TradingSum = "TradingSum"
        OpenPrice = "OpenPrice"
        HighestPrice = "HighestPrice"
        LowestPrice = "LowestPrice"
        MarketCap = "MarketCap"
        SharesOutstanding = "SharesOutstanding"
        EPS = "EPS"
        PER = "PER"
        BPS = "BPS"
        PBR = "PBR"
        DividendPercent = "DividendPercent"
        ForeignHoldingStock = "ForeignHoldingStock"
        ForeignLimitStock = "ForeignLimitStock"
        ShortVolume = "ShortVolume"
        ShortNotional = "ShortNotional"
        
    class TypeEnum(enumerate):
        Value = "Value"
        ChangeAmount = "ChangeAmount"
        RateOfChange = "RateOfChange"
    
    class ConditionEnum(enumerate):
        NONE = "NONE"
        LAG = "LAG"
    
    dataTableMap = {
        DataEnum.ClosePrice : "STOCK_SISAE",
        DataEnum.TradingVolume : "STOCK_SISAE",
        DataEnum.TradingSum : "STOCK_SISAE",
        DataEnum.OpenPrice : "STOCK_SISAE",
        DataEnum.HighestPrice : "STOCK_SISAE",
        DataEnum.LowestPrice : "STOCK_SISAE",
        DataEnum.MarketCap : "STOCK_SISAE",
        DataEnum.SharesOutstanding : "STOCK_SISAE",
        DataEnum.EPS : "STOCK_SISAE",
        DataEnum.PER : "STOCK_SISAE",
        DataEnum.BPS : "STOCK_SISAE",
        DataEnum.PBR : "STOCK_SISAE",
        DataEnum.DividendPercent : "STOCK_SISAE",
        DataEnum.ForeignHoldingStock : "STOCK_SISAE",
        DataEnum.ForeignLimitStock : "STOCK_SISAE",
        DataEnum.ShortVolume : "STOCK_SISAE",
        DataEnum.ShortNotional : "STOCK_SISAE",
    }
    
    typeTableMap = {
        TypeEnum.Value : 2,
        TypeEnum.ChangeAmount : 4,
        TypeEnum.RateOfChange : 5
    }