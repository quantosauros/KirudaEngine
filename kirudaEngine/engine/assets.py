'''
Created on 2015. 6. 16.

@author: Jay
'''

class Asset():

    def __init__(self, assetName, assetCode):
        self.assetName = assetName
        self.assetCode = assetCode
        self.price = 0
        self.prevPrice = 0
        self.weight = 0
        self.prevWeight = 0
        
    def getPrice(self):
        return self.price
    
    def setPrice(self, price):
        self.price = price
    
    def getWeight(self):
        return self.weight
    
    def setPrevWeight(self, prevWeight):
        self.prevWeight = prevWeight
    
    def getPrevWeight(self):
        return self.prevWeight
    
    def setWeight(self, weight):
        self.weight = weight
    
    def getPrevPrice(self):
        return self.prevPrice
    
    def setPrevPrice(self, prevPrice):
        self.prevPrice = prevPrice
    
    def getAssetName(self):
        return self.assetName
    
    def getAssetCode(self):
        return self.assetCode
    