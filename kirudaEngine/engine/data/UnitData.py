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
        query = "SELECT " + self.DataEnum + " FROM " + tableName + " WHERE DATE = " + "'" + date + "'"
        print query
        