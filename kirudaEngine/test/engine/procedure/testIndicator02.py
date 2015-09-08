'''
Created on 2015. 9. 5.

@author: jayjl
'''
from engine.procedure.Indicator import Indicator
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from util.schedule.Date import Date
from engine.type.IndicatorType import IndicatorType
from util.schedule.Vertex import Vertex

import time
from util.DB.stringController import stringController as SC
from engine.procedure.Indicator_MA import Indicator_MA


startTime = time.time()
calendar = SouthKoreaCalendar(1)

asOfDate = Date("20150617")
vertex = Vertex.valueOf("W2")

#indicatorType = IndicatorType.MovingAverage.SimpleMovingAverage5Day
indicatorType = IndicatorType.MovingAverage.WeightedMovingAverage5Day
#indicatorType = IndicatorType.MovingAverage.ExponentialWeightedMovingAverage5Day

indi = Indicator_MA(calendar, asOfDate, vertex, indicatorType)

result = indi.getResult()
print result

#===============================================================================
# for y in result :
#     print y
#===============================================================================

endTime = time.time()
print endTime - startTime



