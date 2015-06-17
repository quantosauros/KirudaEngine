'''
Created on 2015. 6. 16.

@author: Jay
'''

class Asset():

    def __init__(self, assetName, assetCode):
        self.assetName = assetName
        self.assetCode = assetCode

    def getAssetName(self):
        return self.assetName
    
    def getAssetCode(self):
        return self.assetCode
    
    