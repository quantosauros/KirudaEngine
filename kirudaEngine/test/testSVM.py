from sklearn.svm.classes import SVC
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
import csv

iris = datasets.load_iris()
# import some data to play with
f = open('D:\\trainingData.csv','r')
g = open('D:\\resultData.csv','r')

X = []
y = []

trainingData = csv.reader(f)
resultData = csv.reader(g)

for row in trainingData:
    tmpArray = map(float, row)
    X.append(tmpArray)

for col in resultData:
    y.append(col[2])

f.close()
g.close()

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 10.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
lin_svc = svm.LinearSVC(C=C).fit(X, y)

############################################################################

f = open("D:\\trainingData_test.csv","rb")
g = open("D:\\resultData_test.csv","rb")
trainingTestData = csv.reader(f)
resultTestData = csv.reader(g)

testX = []
testY = []

for row in trainingTestData:
#     tmpArray = row.split(',')
    tmpArray = map(float, row)
    testX.append(tmpArray)
 
for col in resultTestData:    
    testY.append(col[2])

f.close()
g.close()

for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    
    Z = clf.predict(testX)    
    #K = clf.cross_validation(X,y)
    #print (clf)
    #print (Z)
    stringTMP = ""
    for kk in Z :
        stringTMP = stringTMP + kk + ", "

    print stringTMP
