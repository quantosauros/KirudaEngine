'''
Created on 2015. 8. 23.

@author: thCho
'''
from util.DB.sqlMap import sqlMap
from lib2to3.fixer_util import String
import AbstractStrategy as AS
import numpy as np
from _mysql import NULL
# from engine.portfolio import Portfolio

class AbstractPortfolioInfo():
    
    def __init__(self, assets, startMoney, period):
#         self.individualPfo = indivPfo
#         stock code
        self.assetArray = assets
        self.addBalance = [False]
        self.Portfolio = []
        self.weight = [[0]]
        self.dailyProfit = [0]
        self.dailyIndividualProfit = []
        self.pfoValue = [0]
        self.balanceValue = startMoney
        self.startDate = period[0]
        self.latestDate = self.startDate
        self.endDate = period[1] 
        tmpTimeStatement = "SELECT DISTINCT(date) FROM STOCK_SISAE WHERE" +  period[0] + " <= date  AND date <= " + period[1] 
        self.timePeriod = self.dbInstance.select(tmpTimeStatement)
        self.timeNum = len(self.timePeriod)
        for i in range(0, len(self.assetArray)):
            self.dailyIndividualProfit.append([0])
            self.weight.append([0])
        
        self.timeArray = {self.timePeriod[0]: 0}
        for i in range(1, self.timeNum):
            self.addBalance.append(False)
            self.timeArray[self.timePeriod[i]] = i
            self.dailyProfit.append(0)
            self.pfoValue.append(0)
            for j in range(0, len(self.assetArray)):
                self.dailyIndividualProfit[j].append(0)
                self.weight[j].append(0)
                
        self.assetIndexMap = {self.assetArray[0]: 0}
        for i in range(1, len(self.assetArray)):
            self.assetIndexMap[self.assetArray[i]] = i
            
        self.historicalStockPrice = []
        for i in range(0, len(self.assetArray)):
#             tmpPriceStatement = sqlMap.SELECTTRAININGDATA %(self.assetArray[i],period[0],period[1])
#             priceData = self.dbInstance.select(tmpPriceStatement)
            priceData = []
            for j in range(0, len(self.timeArray)):
                tmpPriceStatement = sqlMap.SELECTTRAININGDATA %(self.assetArray[i],self.timeArray[j])
                priceData.append(self.dbInstance.select(tmpPriceStatement))
            self.historicalStockPrice.append(priceData)

# same date strategy sorting machine 
    def sortPortfolioWeight(self, strategies):
        strategyNum = len(strategies)
        
        assetIndexToArray = []
        timeIndexToArray = []
        weight =[[]]
        asset = 0
        time = 0
        for i in range(0, len(self.assetArray)):
            assetIndexToArray.append(0)
            timeIndexToArray.append(0)
            weight.append([0])
            for i in range(0, self.timeNum):
                weight[i].append(0)
            
        for i in range(0, strategyNum):
            asset = self.assetIndexMap[strategies[i].returnAssetCode()]
            time = self.timeArray[strategies[i].returnDate()]
            weight[asset][time] = strategies[i].returnWeight()
        
        return [weight]
    
    
    
    def addPortfolioByGP(self, date, weight, netOrInstant):
        cost = 0
        deltaWeight = 0
        
        prevValue = self.balanceValue
        value = 0
        dateIndex = self.timeArray.get(date, -1)
        recentIndex = self.timeArray.get(self.latestDate, -1)
        
        if recentIndex < dateIndex - 1:
            for i in range(recentIndex + 1, dateIndex - 1):
                for j in range(0, len(self.assetArray)):
                    self.weight[j][i] = self.weight[j][i - 1]
        
        if int(date) < int(self.latestDate):
            return NULL
        
        
        for i in range(0, len(self.assetArray)):
            assetPrice = self.historicalStockPrice[i][dateIndex]
            prevValue += assetPrice * weight[i]
            
        
        if netOrInstant == False:
            for i in range(0, len(self.assetArray)):
                if dateIndex > -1 :
                    assetPrice = self.historicalStockPrice[i][dateIndex]
                    cost += assetPrice * weight[i]
                    self.weight[i][dateIndex] = self.weight[i][dateIndex - 1] + weight[i]
                else :
                    self.weight[i][dateIndex] += 0
                    cost = 0
                value += self.weight[i][dateIndex] * assetPrice
        else :
            for i in range(0, len(self.assetArray)):
                if dateIndex > 0 :
                    assetPrice = self.historicalStockPrice[i][dateIndex]
                    deltaWeight = weight[i] - self.weight[i][dateIndex - 1]
                    cost += assetPrice * deltaWeight
                    self.weight[i][dateIndex] = weight[i]
                elif dateIndex == 0 :
                    cost += assetPrice * weight[i]
                    self.weight[i][0] = self.weight[i][0] 
                else :
                    self.weight[i][dateIndex] += 0
                    cost = 0
                value += self.weight[i][dateIndex] * assetPrice
        
        self.balanceValue -= cost
        self.latestDate = date
        self.pfoValue[dateIndex] = self.balanceValue + value
        self.dailyProfit[dateIndex] = value - prevValue
        
        
    def putMoney(self, date, money):
        dateIndex = self.timeArray.get(date, -1)
        self.balanceValue += money
        self.addBalance[dateIndex] == True
        
    def MarkToMark(self, date):
        dateIndex = self.timeArray.get(date, -1)
        
        return self.dailyProfit[dateIndex]
    
    def IndividualProfit(self, asset, period):
        dateStartIndex = self.timeArray.get(period[0], -1)
        dateEndIndex = self.timeArray.get(period[1], -1)
        profit = 0
        assetIndex = self.assetIndexMap[asset]
        profitSum = 0
        for i in range(dateStartIndex, dateEndIndex + 1):
            tmpProfit = 0
            if i == 0:
                tmpProfit = 0
            else:
                tmpProfit = (self.historicalStockPrice[assetIndex][i + 1] - self.historicalStockPrice[assetIndex][i]) * self.weight[assetIndex][i]
            profit += tmpProfit
            self.dailyIndividualProfit[assetIndex][i] += profit
            profitSum += profit         
        return profitSum
    
    def StrategyProfitMomentum(self, period, meanOrVariance):
        dateStartIndex = self.timeArray.get(period[0], -1)
        dateEndIndex = self.timeArray.get(period[1], -1)
        periodProfit = []
        for i in range(dateStartIndex, dateEndIndex):
            periodProfit.append(self.dailyProfit[i])
            
        mean = np.mean(periodProfit)
        variance = np.std(periodProfit)
        return [mean, variance]
        
    
    def returnWeightMtx(self):
        return self.weight
    
    
        
        