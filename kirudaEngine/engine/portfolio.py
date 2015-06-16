'''
Created on 2015. 6. 16.

@author: Jay
'''

class PortFolio():
    
    def __init__(self, assets):
        self.assets = assets
        self.size = len(self.assets)
       
    def getCurrentValue(self):
        sum = 0
        for index in range(0, self.size) :
            weight = self.assets[index].getWeight()
            price = self.assets[index].getPrice()
            sum = sum + weight * price
            
        return sum
    
    def getPrevValue(self):
        sum = 0
        for index in range(0, self.size) :
            weight = self.assets[index].getPrevWeight()
            price = self.assets[index].getPrevPrice()
            sum = sum + weight * price
            
        return sum
    
    def getBalance(self):
        sum = 0
        for index in range(0, self.size) :
            prevWeight = self.assets[index].getPrevWeight()
            currWeight = self.assets[index].getWeight()
            price = price = self.assets[index].getPrice()
            sum = sum + (currWeight - prevWeight) * price
        
        return sum
    
    def getProfit(self):
        sum = 0
        for index in range(0, self.size) :
            weight = self.assets[index].getPrevWeight()
            prevPrice = self.assets[index].getPrevPrice()
            currPrice = price = self.assets[index].getPrice()
            sum = sum + weight * (currPrice - prevPrice)
        
        return sum

    