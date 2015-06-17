'''
Created on 2015. 6. 16.

@author: Jay
'''
from engine.portfolio import Portfolio
from engine.assets import Asset

asset1 = Asset(assetName = "APPLE", assetCode = "AAPL")
asset2 = Asset(assetName = "GOOGLE", assetCode = "GGLE")

assets = (asset1, asset2)
periods = ("20150617" , "20150618", "20150619")

pfo = Portfolio(assets, periods, 0)

prices = ((5,6,5),(10,10,11))
weights = ((1,2,1),(3,3,4))

pfo.setData(prices, weights)
#===============================================================================
# pfo.setPrices(prices)
# pfo.setWeights(weights)
#===============================================================================

for index in range(0, len(periods)):    
    pfoValue = pfo.getPfoValue(index)
    profit = pfo.getProfit(index)
    balance = pfo.getBalance(index)
    print("PfoValue at " + repr(periods[index]) + " : " + str(pfoValue))
    print("Profit at " + repr(periods[index]) + " : " + str(profit))
    print("Balance at " + repr(periods[index]) + " : " + str(balance))



