'''
Created on 2015. 8. 12.

@author: Jay
'''
from engine.data.UnitData import UnitData
from engine.selectAssets import SelectAsset
from util.assetConditions import assetConditions
from util.dataEnums import dataEnums
from engine.data.AbstractData import AbstractData
from util.QueryMaker import QueryMaker
from util.Date import Date
from util.SouthKoreaCalendar import SouthKoreaCalendar
from util.BusinessDayConvention import BusinessDayConvention




date1 = Date('20150815')
date2 = Date.valueOf('19860111')

calen = SouthKoreaCalendar.getCalendar(0)
print calen.isHoliday(date1)
print calen.adjustDate(date1, BusinessDayConvention.MODIFIED_FOLLOWING)

periods = [Date('20150611'), Date('20150612'), Date('20150617'),]
#Assets
sa = SelectAsset()
variables = [assetConditions.MARKET]
conditions = ["='KQ'"]
#variables = [assetConditions.CODE]
#conditions = [" in ('KS005930', 'KS008770')"]
#variables = [assetConditions.MARKET, assetConditions.PER]
#conditions = ["='KQ'", ">'9'"]
assets = sa.select(variables, conditions, Date('20150617'))
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

#===============================================================================
# #Assets
# sa = SelectAsset()
# variables = [assetConditions.MARKET]
# conditions = ["='KQ'"]
# #variables = [assetConditions.CODE]
# #conditions = [" in ('KS005930', 'KS008770')"]
# #variables = [assetConditions.MARKET, assetConditions.PER]
# #conditions = ["='KQ'", ">'9'"]
# assets = sa.select(variables, conditions)
# 
# date = "20150601"
# unitdata = UnitData(dat, date, assets)
# unitdata.getResult()
#===============================================================================
