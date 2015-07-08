'''
Created on 2015. 6. 16.

@author: Jay
'''

class Portfolio():
    '''
    PFO VALUE = STOCK VALUE + BALANCE
    '''
    def __init__(self, assets, periods, initialBalance):
        self.assets = assets
        self.pfoNum = len(self.assets)
        self.periods = periods
        self.periodNum = len(self.periods)
        self.initialBalance = initialBalance
        self.pfoValues = {}
        self.balances = {}
                
    def init(self):
        #pfo value        
        for timeIndex in range(0, self.periodNum) :            
            pfoSum = 0
            balanceSum = 0
            for assetIndex in range(0, self.pfoNum) :
                prevWeight = self.weights[assetIndex][timeIndex - 1]
                currWeight = self.weights[assetIndex][timeIndex]
                
                price = self.prices[assetIndex][timeIndex]
                
                #print (self.periods[timeIndex], self.assets[assetIndex].getAssetCode(), price)
                
                pfoSum = pfoSum + currWeight * price
                balanceSum = balanceSum - (currWeight - prevWeight) * price           
                        
            if timeIndex is 0 :
                self.balances[timeIndex] = self.initialBalance
            else :
                self.balances[timeIndex] = self.balances[timeIndex - 1] + balanceSum
                
            self.pfoValues[timeIndex] = pfoSum + self.balances[timeIndex]
    
    def setData(self, prices, weights):
        self.setPrices(prices)
        self.setWeights(weights)
        self.init()
    
    def setPrices(self, prices):
        self.prices = prices
    
    def setWeights(self, weights):
        self.weights = weights
    
    def getPfoValue(self, time):
        #find timeIndex wrt time
        timeIndex = time      
        return self.pfoValues[timeIndex]

    def getBalance(self, time):
        #find timeIndex wrt time
        timeIndex = time
        return self.balances[timeIndex]
    
    def getProfit(self, time):
        #find timeIndex wrt time
        timeIndex = time
        if timeIndex is 0 :
            return 0
        else :
            return self.pfoValues[timeIndex] - self.pfoValues[timeIndex - 1]

    