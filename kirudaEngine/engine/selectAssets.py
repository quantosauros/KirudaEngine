'''
Created on 2015. 6. 18.

@author: Jay
'''
from engine.assets import Asset
from util.DB.dbConnector import dbConnector
from util.DB.sqlMap import sqlMap
from engine.type.PortfolioType import PortfolioType

class SelectAsset():

    def __init__(self):
        self.dbInstance = dbConnector(sqlMap.connectInfo)
        self.AssetList = []
        
    def select(self, variables, conditions, date):
        '''
        
        '''   
         
        selectStatement = "\
            SELECT \
                B.CODE, B.NAME \
            FROM "
            
        fromStatement = ""
        for x in PortfolioType.tableMap:
            tmp = x + " " + PortfolioType.tableMap[x] + ", "
            fromStatement = fromStatement + tmp
            #print(tmp)
        
        whereStatement = "\
             WHERE \
                A.CODE = B.CODE \
                AND A.DATE = '%s'\
            " %(date.getDate())
            
        totalStatement = selectStatement + fromStatement[:-2] + whereStatement
        for index in range(0, len(variables)):
            tableName = PortfolioType.conditionTable[variables[index]]
            condition = " AND " + PortfolioType.tableMap[tableName] + "." +\
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
        '''
        test method
        '''
        assetNames  = ("SAMSUNG ELCT", "HOTEL SILLA", "CJE&M")
        assetCodes = ("KS005930", "KS008770", "KQ130960")
        #assetNames  = ("SAMSUNG ELCT", )
        #assetCodes = ("KS000080", )
        
        
        length = len(assetCodes)
        
        for index in range(0, length):
            self.AssetList.append(Asset(assetNames[index], assetCodes[index]))
        
        return self.AssetList