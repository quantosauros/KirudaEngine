'''
Created on 2015. 8. 12.

@author: Jay
'''
from engine.selectAssets import SelectAsset
from engine.data.AbstractData import AbstractData
from util.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from util.schedule.Period import Period
from util.schedule.Vertex import Vertex
from util.schedule.Date import Date
from engine.type.PortfolioType import PortfolioType
from engine.type.TrainingDataType import TrainingDataType

asOfDate = Date("20150622")
calendar = SouthKoreaCalendar(0)
pp = Period(asOfDate, calendar)
periods = pp.getPeriodByVertex(Vertex.valueOf("D1"))
for x in periods :
    print x


#periods = [Date('20150611'), Date('20150612'), Date('20150617'),]
#Assets
sa = SelectAsset()
variables = [PortfolioType.MARKET]
conditions = ["='KQ'"]
#variables = [assetConditions.CODE]
#conditions = [" in ('KS005930', 'KS008770')"]
#variables = [assetConditions.MARKET, assetConditions.PER]
#conditions = ["='KQ'", ">'9'"]
assets = sa.select(variables, conditions, asOfDate)
#assets = sa.selectTest()

dats = [TrainingDataType.DataEnum.ClosePrice, TrainingDataType.DataEnum.TradingVolume]
dataTypes = [TrainingDataType.TypeEnum.Value, TrainingDataType.TypeEnum.ChangeAmount]
dataCondiTypes = [TrainingDataType.ConditionEnum.NONE, TrainingDataType.ConditionEnum.LAG]
dataConditions = [-3, -1]

dataClass = AbstractData(assets, dats, dataTypes, dataCondiTypes, dataConditions)
result = dataClass.getResult(calendar, periods)

for x in result :
    for y in x :
        print y
        print len(y)
        
#[date][data][stockCode][column]
print result[0][0]
print result[1][0]
print result[0][1]
#print result[0][0][0]
#print result[0][0][1]
#print result[0][0][1][1]
#print result[0][0][1][2]


