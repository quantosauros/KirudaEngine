'''
Created on 2015. 9. 3.

@author: Jay
'''
from util.schedule.Date import Date
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from engine.type.IndicatorType import IndicatorType
from util.schedule.Vertex import Vertex
import time
from engine.procedure.Indicator_MA import Indicator_MA

startTime = time.time()
#Simple Moving Average 5 Day
calendar = SouthKoreaCalendar(1)
asOfDate = Date("20150617")

vertex = Vertex.valueOf("M6")

#print date
for i, aa in enumerate((
                     IndicatorType.IndicatorType_MA.SimpleMovingAverage5Day,
                     #IndicatorType.IndicatorType_MA.SimpleMovingAverage20Day,                         
                     #IndicatorType.IndicatorType_MA.SimpleMovingAverage60Day,
                     #IndicatorType.IndicatorType_MA.SimpleMovingAverage120Day,
                     #IndicatorType.IndicatorType_MA.WeightedMovingAverage5Day,
                     #IndicatorType.IndicatorType_MA.WeightedMovingAverage20Day,
                     #IndicatorType.IndicatorType_MA.WeightedMovingAverage60Day,
                     #IndicatorType.IndicatorType_MA.WeightedMovingAverage120Day,
                     #IndicatorType.IndicatorType_MA.ExponentialWeightedMovingAverage5Day,
                     #IndicatorType.IndicatorType_MA.ExponentialWeightedMovingAverage20Day,
                     #IndicatorType.IndicatorType_MA.ExponentialWeightedMovingAverage60Day,
                     #IndicatorType.IndicatorType_MA.ExponentialWeightedMovingAverage120Day
                     )) :
    
    indicatorType = aa
    #print IndicatorType
    
    indi = Indicator_MA(calendar, asOfDate, vertex, indicatorType)
    indi.insertResult()
    #print indi.getResult()

endTime = time.time()
print endTime - startTime

