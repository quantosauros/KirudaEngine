'''
Created on 2015. 6. 16.

@author: Jay
'''
from engine.portfolio import PortFolio
from engine.assets import Asset

asset1 = Asset(assetName = "APPLE", assetCode = "AAPL")
asset1.setPrevPrice(10)
asset1.setPrice(8)
asset1.setPrevWeight(3)
asset1.setWeight(1)


asset2 = Asset(assetName = "GOOGLE", assetCode = "GGLE")
asset2.setPrevPrice(5)
asset2.setPrice(12)
asset2.setPrevWeight(1)
asset2.setWeight(5)

assets = (asset1, asset2)

pfo = PortFolio(assets)

prevValue = pfo.getPrevValue()
print("PrevValue: " + str(prevValue))
currentValue = pfo.getCurrentValue()
print("CurrentValue: " + str(currentValue))

profit = pfo.getProfit()
print("Profit :" + str(profit))

balance = pfo.getBalance()
print("Balance: " + str(balance))
