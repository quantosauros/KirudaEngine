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
                     IndicatorType.MovingAverage.SimpleMovingAverage5Day,
                     #IndicatorType.MovingAverage.SimpleMovingAverage20Day,                         
                     #IndicatorType.MovingAverage.SimpleMovingAverage60Day,
                     #IndicatorType.MovingAverage.SimpleMovingAverage120Day,
                     #IndicatorType.MovingAverage.WeightedMovingAverage5Day,
                     #IndicatorType.MovingAverage.WeightedMovingAverage20Day,
                     #IndicatorType.MovingAverage.WeightedMovingAverage60Day,
                     #IndicatorType.MovingAverage.WeightedMovingAverage120Day,
                     #IndicatorType.MovingAverage.ExponentialWeightedMovingAverage5Day,
                     #IndicatorType.MovingAverage.ExponentialWeightedMovingAverage20Day,
                     #IndicatorType.MovingAverage.ExponentialWeightedMovingAverage60Day,
                     #IndicatorType.MovingAverage.ExponentialWeightedMovingAverage120Day
                     )) :
    
    indicatorType = aa
    #indicatorType = IndicatorType.MovingAverage.ExponentialWeightedMovingAverage5Day
    #print IndicatorType
    
    indi = Indicator_MA(calendar, asOfDate, vertex, indicatorType)
    indi.insertResult()
    #print indi.getResult()

endTime = time.time()
print endTime - startTime

