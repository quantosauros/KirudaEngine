'''
Created on 2015. 9. 11.

@author: thCho
'''

import engine.portfolioInfo.PortfolioInfo as PI
import engine.portfolioInfo.AbstractStrategy as ASt
from engine.portfolio.SelectAssets import SelectAsset
from engine.type.PortfolioType import PortfolioType
from util.schedule.Date import Date
from util.schedule.Period import Period

today = Date('20150611')
#Assets
sa = SelectAsset()
variables = [PortfolioType.MARKET, PortfolioType.MARKETCAP]
conditions = ["='KS'", ">= '50000000'"]

assets = sa.select(variables, conditions, today)
assetCodes = []
for i in range(0, len(assets)):
    assetCodes.append(assets[i].assetCode)
initialMoney = 1.0E6
period = ['20150105','20150113']

portfolio = PI.PortfolioInfo(assetCodes, initialMoney, period)

strategy = []
for i in range(0, len(assets)):
    if i%4 == 0:
        strategy.append(ASt.AbstractStrategy('20150105', assetCodes[i], 1))
        
    if i%4 == 0:
        strategy.append(ASt.AbstractStrategy('20150113', assetCodes[i], -1))


portfolio.getInfobyStrategy(strategy, False)

dates = ['20150106', '20150107', '20150108', '20150109']
for i in range(0, len(dates)):
    print(portfolio.getMTM(dates[i]))


