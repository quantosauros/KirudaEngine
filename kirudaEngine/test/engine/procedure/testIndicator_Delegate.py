#-*- coding: utf-8 -*-
'''
Created on 2015. 9. 10.

@author: Jay
'''
from util.schedule.Date import Date
from util.schedule.Vertex import Vertex
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from engine.type.IndicatorType import IndicatorType

import time
from engine.procedure.IndicatorGenerator import IndicatorGenerator

startTime = time.time()
calendar = SouthKoreaCalendar(1)

asOfDate = Date("20150617")
vertex = Vertex.valueOf("W2")

#indicatorType = IndicatorType.IndicatorType_MA.SimpleMovingAverage5Day
#indicatorType = IndicatorType.IndicatorType_Volatility.Volatility5Day
indicatorType = IndicatorType.IndicatorType_MA.ExponentialWeightedMovingAverage5Day

indi = IndicatorGenerator(calendar, asOfDate, vertex, indicatorType)

#indi = Indicator_Volatility(calendar, asOfDate, vertex, indicatorType)

result = indi.getResult()
assets = indi.getAssetList()
for i in range(0, len(result)) :
    print assets[i]
    print result[i]
    
    