#-*- coding: utf-8 -*-
'''
Created on 2015. 9. 8.

@author: Jay
'''
from engine.procedure.Indicator_Volatility import Indicator_Volatility
import time
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from util.schedule.Date import Date
from util.schedule.Vertex import Vertex
from engine.type.IndicatorType import IndicatorType

startTime = time.time()
calendar = SouthKoreaCalendar(1)

asOfDate = Date("20150617")
vertex = Vertex.valueOf("M1")

#indicatorType = IndicatorType.MovingAverage.SimpleMovingAverage5Day
indicatorType = IndicatorType.IndicatorType_Volatility.Volatility5Day
#indicatorType = IndicatorType.MovingAverage.ExponentialWeightedMovingAverage5Day

indi = Indicator_Volatility(calendar, asOfDate, vertex, indicatorType)

result = indi.getResult()
assets = indi.getAssetList()
for i in range(0, len(result)) :
    print assets[i]
    print result[i]
    
    
    
    