'''
Created on 2015. 8. 12.

@author: Jay
'''
from util.dataEnums import dataEnums

class UnitData():
    
    def __init__(self, DataEnum, Date, Assets):
        self.DataEnum = DataEnum
        self.Date = Date
        
    def getResult(self):
        tableName = dataEnums.tableMap[self.DataEnum]
        date = self.Date
        query = "CALL PC_TEST1('" + self.DataEnum + "', '" + tableName + "'," + date.getDate() + date.plusDays(1).getDate() + "  , "'KS005930','KS008770'");"
        print query
        