'''
Created on 2015. 9. 10.

@author: Jay
'''
from engine.procedure.AbstractIndicator import DelegateIndicator
from engine.type.IndicatorType import IndicatorType
from engine.procedure.Indicator_MA import Indicator_MA
from engine.procedure.Indicator_AD import Indicator_AD
from engine.procedure.Indicator_Volatility import Indicator_Volatility
 
class IndicatorGenerator(DelegateIndicator):
    
    def __init__(self, calendar, asOfDate, vertex, indicatorType):
        
        if indicatorType in IndicatorType.IndicatorType_MA.list :
            delegate = Indicator_MA(calendar, asOfDate, vertex, indicatorType)
        elif indicatorType in IndicatorType.IndicatorType_AD.list :
            delegate = Indicator_AD(calendar, asOfDate, vertex, indicatorType)
        elif indicatorType in IndicatorType.IndicatorType_Volatility.list :
            delegate = Indicator_Volatility(calendar, asOfDate, vertex, indicatorType)
        else :
            None
            
        self.setDeletage(delegate)
            
            
    @staticmethod
    def getIndicator(calendar, asOfDate, vertex, indicatorType):
        if indicatorType in IndicatorType.IndicatorType_MA.list :
            return IndicatorGenerator(calendar, asOfDate, vertex, indicatorType)
        else :
            return IndicatorGenerator(calendar, asOfDate, vertex, indicatorType)
        
        