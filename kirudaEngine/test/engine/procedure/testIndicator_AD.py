'''
Created on 2015. 9. 7.

@author: Jay
'''
import time
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from util.schedule.Date import Date
from util.schedule.Vertex import Vertex
from engine.type.IndicatorType import IndicatorType
from engine.procedure.Indicator_AD import Indicator_AD

startTime = time.time()
calendar = SouthKoreaCalendar(1)

asOfDate = Date("20150617")
vertex = Vertex.valueOf("W1")

#indicatorType = IndicatorType.MovingAverage.SimpleMovingAverage5Day
indicatorType = IndicatorType.IndicatorType_AD.AccumulationDistricutionIndex
#indicatorType = IndicatorType.MovingAverage.ExponentialWeightedMovingAverage5Day

indi = Indicator_AD(calendar, asOfDate, vertex, indicatorType)

result = indi.getResult()
for x in result :
    print x