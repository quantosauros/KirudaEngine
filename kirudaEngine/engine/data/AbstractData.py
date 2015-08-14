'''
Created on 2015. 8. 12.

@author: Jay
'''
from engine.data.UnitData import UnitData
from util.dataEnums import dataEnums

class AbstractData():
        
    def __init__(self, assets, data, dataType, condiType, condition = ""):
        self.data = data
        self.dataType = dataType
        self.condiType = condiType
        self.condition = condition
        self.Assets = assets
        self.numOfData = len(data)
        
    def getResult(self, date):
        tableNames = ""
        columnNames = ""
        for index in range(0, self.numOfData):
            data = self.data[index]
            dataType = self.dataType[index]
            condiType = self.condiType[index]
            condition = self.condition[index]
                        
            tableName = dataEnums.tableMap[data]
            columnName = data
            tableNames = tableNames + tableName
            columnNames = columnNames + columnName
            
            if dataType is dataEnums.TypeEnum.Value :
                print "A"
                tmp = UnitData(data, date, self.Assets)
                tmp.getResult()
                
            elif dataType is dataEnums.TypeEnum.ChangeAmount : 
                print "B"            
                tmp1 = UnitData(data, date, self.Assets)
                tmp1.getResult()
                tmp2 = UnitData(data, date + condition, self.Assets)
                tmp2.getResult()
                
            elif dataType is dataEnums.TypeEnum.RateOfChange :
                print "C"
                tmp = UnitData(data, date, self.Assets)
                tmp.getResult()
        
        print tableNames + "; " + columnNames
        return self.data + self.dataType + self.condiType + self.condition
    
    
        