'''
Created on 2015. 6. 22.

@author: thCho
'''
from svmutil import *
import csv


trainingMtx = []
rstMtx = []
rstTmp = []
f = open('D:\\trainingData.csv','r')
g = open('D:\\resultData.csv','r')
trainingData = csv.reader(f)
resultData = csv.reader(g)
i=0

for row in trainingData:
#     tmpArray = row.split(',')
    tmpArray = map(float, row)
    trainingMtx.append(tmpArray)

    
#     print(row)

for col in resultData:
    rstMtx.append(col)
    rstTmp.append(col[2])
#     print(col)
f.close()
g.close()

# trainingData = csv.reader(file('trainingData.csv','r'))
# resultData = csv.reader(file('resultData.csv','r'))

svm_model.predict = lambda self, x: svm_predict([0], [x], self)[0][0]
rstTmp = map(int, rstTmp)

prob = svm_problem(rstTmp, trainingMtx)

param = svm_parameter()
param.kernel_type = LINEAR
param.C = 10
param.parse_options('-b 1')
print("START!!!")
m=svm_train(prob, param)

TestMtx = []
rstTestMtx = []
rstTestTmp = []
f = open("D:\\trainingData_test.csv","rb")
g = open("D:\\resultData_test.csv","rb")
trainingTestData = csv.reader(f)
resultTestData = csv.reader(g)
 
for row in trainingTestData:
#     tmpArray = row.split(',')
    tmpArray = map(float, row)
    TestMtx.append(tmpArray)
#     print(row)
 
for col in resultTestData:
    rstTestMtx.append(col)
    rstTestTmp.append(col[2])
#     print(col)

rstTestTmp = map(int, rstTestTmp)
f.close()
g.close()
 
dd = svm_predict(rstTestTmp, TestMtx, m, '-b 1')
 
print(dd[0])
print(dd[2])



