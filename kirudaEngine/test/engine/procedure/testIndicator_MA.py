'''
Created on 2015. 9. 5.

@author: jayjl
'''
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from util.schedule.Date import Date
from engine.type.IndicatorType import IndicatorType
from util.schedule.Vertex import Vertex
import time
from engine.procedure.Indicator_MA import Indicator_MA


startTime = time.time()
calendar = SouthKoreaCalendar(1)

asOfDate = Date("20150617")
vertex = Vertex.valueOf("W2")

#indicatorType = IndicatorType.IndicatorType_MA.SimpleMovingAverage5Day
indicatorType = IndicatorType.IndicatorType_MA.WeightedMovingAverage5Day
#indicatorType = IndicatorType.IndicatorType_MA.ExponentialWeightedMovingAverage5Day

indi = Indicator_MA(calendar, asOfDate, vertex, indicatorType)

result = indi.getResult()
print result

#===============================================================================
# for y in result :
#     print y
#===============================================================================

endTime = time.time()
print endTime - startTime



