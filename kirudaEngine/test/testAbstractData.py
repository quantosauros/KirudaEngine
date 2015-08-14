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

periods = ['20150611','20150612','20150615','20150616','20150617', '20150618']
#Assets
sa = SelectAsset()
variables = [assetConditions.MARKET]
conditions = ["='KQ'"]
#variables = [assetConditions.CODE]
#conditions = [" in ('KS005930', 'KS008770')"]
#variables = [assetConditions.MARKET, assetConditions.PER]
#conditions = ["='KQ'", ">'9'"]
assets = sa.select(variables, conditions, '20150617')


dats = [dataEnums.DataEnum.ClosePrice, dataEnums.DataEnum.TradingVolume]
dataTypes = [dataEnums.TypeEnum.Value, dataEnums.TypeEnum.ChangeAmount]
dataCondiTypes = [dataEnums.ConditionEnum.NONE, dataEnums.ConditionEnum.LAG]
dataConditions = ["", "-1"]

dataClass = AbstractData(assets, dats, dataTypes, dataCondiTypes, dataConditions)
dataClass.getResult(periods[1])

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
