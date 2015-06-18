'''
Created on 2015. 6. 18.

@author: Jay
'''
from engine.selectAssets import SelectAsset


aa = SelectAsset()

list = aa.select()

for x in list:
    print(x)