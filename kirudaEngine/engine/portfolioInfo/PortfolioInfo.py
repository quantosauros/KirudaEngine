'''
Created on 2015. 8. 23.

@author: thCho
'''
import AbstractPortfolioInfo as PI
import AbstractStrategy as AS
from util.sqlMap import sqlMap
from lib2to3.fixer_util import String
import numpy as np
from _mysql import NULL

# from engine.portfolio import Portfolio

class PortfolioInfo():
    
    def __init__(self, assets, startMoney, period):
        self.asset = assets
        self.balance = startMoney
        self.period = period
        self.Pfo = PI(assets, startMoney, period)
    
    
    def getInfobyStrategy(self, strategies, netOrInstant):
        for i in range(0, self.Pfo.timeNum):
            date = self.Pfo.timePeriod[i]
            tmpWeight = self.Pfo.sortPortfolioWeight(strategies)
            weight = []
            for j in range(0, len(self.Pfo.assetArray)):
                weight.append(tmpWeight[j][i])
            self.Pfo.addPortfolioByGP(date, weight, netOrInstant) 
        
    def getInfobyGp(self, weight, netOrInstant):
        for i in range(0, self.Pfo.timeNum):
            date = self.Pfo.timePeriod[i]
            tmpWeight = []
            for j in range(0, len(self.Pfo.assetArray)):
                tmpWeight.append(weight[j][i])
            self.Pfo.addPortfolioByGP(date, tmpWeight, netOrInstant)
    
    
        