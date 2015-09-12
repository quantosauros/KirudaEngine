'''
Created on 2015. 9. 10.

@author: thCho
'''


class AbstractStrategy():
    
    def __init__(self, date, assetCode, weight):
        self.assetCode = assetCode
        self.date = date
        self.weight = weight
        
    def returnAssetCode(self):
        return self.assetCode
    
    def returnDate(self):
        return self.date
    
    def returnWeight(self):
        return self.weight