'''
Created on 2015. 8. 12.

@author: Jay
'''
from engine.data.UnitData import UnitData
from util.dataEnums import dataEnums

class AbstractData():
        
    def __init__(self, data, dataType, condiType, condition = ""):
        self.data = data
        self.dataType = dataType
        self.condiType = condiType
        self.condition = condition
        self.Assets = ""
        
    def getResult(self, date):
        if self.dataType is dataEnums.TypeEnum.Value :
            print "A"
            tmp = UnitData(self.data, date, self.Assets)
            tmp.getResult()
            
        elif self.dataType is dataEnums.TypeEnum.ChangeAmount : 
            print "B"            
            tmp1 = UnitData(self.data, date, self.Assets)
            tmp1.getResult()
            tmp2 = UnitData(self.data, date + self.condition, self.Assets)
            tmp2.getResult()
            
        elif self.dataType is dataEnums.TypeEnum.RateOfChange :
            print "C"
            tmp = UnitData(self.data, date, self.Assets)
            tmp.getResult()
            
        return self.data + self.dataType + self.condiType + self.condition
    
    
        