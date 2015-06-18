'''
Created on 2015. 6. 16.

@author: Jay
'''
from engine.assets import Asset
from engine.historicalData import HistoricalData
from engine.portfolio import Portfolio
from engine.selectAssets import SelectAsset
from util.assetConditions import assetConditions

#Assets
sa = SelectAsset()
assets = sa.selectTest()
#print(assets)
variables = [assetConditions.MARKET]
conditions = ["='KQ'"]
#variables = [assetConditions.MARKET, assetConditions.PER]
#conditions = ["='KQ'", ">'9'"]
assets = sa.select(variables, conditions)
for x in assets:
    print(x)

#Periods
periods = ["20150617", '20150618']

#Weight
weights = []
for assetIndex in range(0, len(assets)):
    tmpWeight = []
    for timeIndex in range(0, len(periods)):
        tmpWeight.append(1)    
        
    weights.append(tmpWeight)

#Historical Prices
hd = HistoricalData()
prices = hd.getStockPrices(assets, periods)

#Portfolio
pfo = Portfolio(assets, periods, 0)
pfo.setData(prices, weights)

for index in range(0, len(periods)):    
    pfoValue = pfo.getPfoValue(index)
    profit = pfo.getProfit(index)
    balance = pfo.getBalance(index)
    print("PfoValue at " + repr(periods[index]) + " : " + str(pfoValue))
    print("Profit at " + repr(periods[index]) + " : " + str(profit))
    print("Balance at " + repr(periods[index]) + " : " + str(balance))



