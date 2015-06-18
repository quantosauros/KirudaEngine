'''
Created on 2015. 6. 18.

@author: Jay
'''
from engine.assets import Asset
from util.dbConnector import dbConnector
from util.sqlMap import sqlMap
from util.assetConditions import assetConditions

class SelectAsset():

    def __init__(self):
        self.dbInstance = dbConnector(sqlMap.connectInfo)
        self.AssetList = []
        
    def select(self, variables, conditions):    
        date = '20150617'   
         
        selectStatement = "\
            SELECT \
                B.CODE, B.NAME \
            FROM "
            
        fromStatement = ""
        for x in assetConditions.tableMap:
            tmp = x + " " + assetConditions.tableMap[x] + ", "
            fromStatement = fromStatement + tmp
            #print(tmp)
        
        whereStatement = "\
             WHERE \
                A.CODE = B.CODE \
                AND A.DATE = '%s'\
            " %(date)
            
        totalStatement = selectStatement + fromStatement[:-2] + whereStatement
        for index in range(0, len(variables)):
            tableName = assetConditions.conditionTable[variables[index]]
            condition = " AND " + assetConditions.tableMap[tableName] + "." +\
                variables[index] + conditions[index] 
                        
            #print(condition)
            totalStatement = totalStatement + condition
        
        #print(totalStatement)
        
        assetList = self.dbInstance.select(totalStatement)
        
        #print(assetList)
        
        for index in range(0, len(assetList)):
            #print(assetList[index][0])
            #print(assetList[index][1])
            self.AssetList.append(Asset(assetList[index][1], assetList[index][0]))
        
        return self.AssetList
        
        
    def selectTest(self):
        assetNames  = ("SAMSUNG ELCT", "HOTEL SILLA")
        assetCodes = ("KS005930", "KS008770")
        
        length = 2
        
        for index in range(0, 2):
            self.AssetList.append(Asset(assetNames[index], assetCodes[index]))
        
        return self.AssetList