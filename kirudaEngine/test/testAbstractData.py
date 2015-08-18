'''
Created on 2015. 8. 12.

@author: Jay
'''
from engine.selectAssets import SelectAsset
from util.assetConditions import assetConditions
from util.dataEnums import dataEnums
from engine.data.AbstractData import AbstractData
from util.Date import Date
from util.Period import Period
from util.SouthKoreaCalendar import SouthKoreaCalendar
from util.Vertex import Vertex

asOfDate = Date("20150622")
calendar = SouthKoreaCalendar(0)
pp = Period(asOfDate, Vertex.valueOf("M3"), calendar)
periods = pp.getPeriod()
for x in periods :
    print x


#periods = [Date('20150611'), Date('20150612'), Date('20150617'),]
#Assets
sa = SelectAsset()
variables = [assetConditions.MARKET]
conditions = ["='KQ'"]
#variables = [assetConditions.CODE]
#conditions = [" in ('KS005930', 'KS008770')"]
#variables = [assetConditions.MARKET, assetConditions.PER]
#conditions = ["='KQ'", ">'9'"]
assets = sa.select(variables, conditions, asOfDate)
#assets = sa.selectTest()

dats = [dataEnums.DataEnum.ClosePrice, dataEnums.DataEnum.TradingVolume]
dataTypes = [dataEnums.TypeEnum.Value, dataEnums.TypeEnum.ChangeAmount]
dataCondiTypes = [dataEnums.ConditionEnum.NONE, dataEnums.ConditionEnum.LAG]
dataConditions = [0, -1]

dataClass = AbstractData(assets, dats, dataTypes, dataCondiTypes, dataConditions)
result = dataClass.getResult(periods)

for x in result :
    for y in x :
        print y
        print len(y)

print result[0][0][1]
print result[0][0][1][1]


