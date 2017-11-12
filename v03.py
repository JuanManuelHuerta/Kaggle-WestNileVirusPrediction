import numpy as np
from sklearn import ensemble, preprocessing, linear_model
from KS import compute_KS
from sklearn.metrics import roc_auc_score
import csv


# Load dataset 
#weather = pd.read_csv('../input/weather.csv')

'''
This is the first Logistic Regression approach
'''

## Mapper for dummy variables (categorical to dummy)

f_matrix= [['Species',"CULEX PIPIENS",0],
           ['Species',"CULEX PIPIENS/RESTUANS",1],
           ['Species',"CULEX RESTUANS",2],
           ['Species',"CULEX SALINARIUS",3],
           ['Species',"CULEX TARSALIS",3],
           ['Species',"CULEX TERRITANS",3]]


def featurize(l,h):
    v=[0.0]*4
    for line in f_matrix:
        if l[h[line[0]]]==line[1]:
            v[line[2]]=1.0
    return v




fp = open('../input/train.v02.csv')
h1=fp.readline().replace("\"","").rstrip().split(",")
header_1={x[0]:x[1] for x in zip(h1,range(len(h1)))}
train_raw=[]
train=[]
train_label=[]
for line in csv.reader(fp):
    train_raw.append(line)
    train.append(featurize(line,header_1))
    train_label.append(int(line[header_1['WnvPresent']]))
fp.close()


fp = open('../input/test.v02.csv')
h2=fp.readline().replace("\"","").rstrip().split(",")
header_2={x[0]:x[1] for x in zip(h2,range(len(h2)))}
test_raw=[]
test=[]
test_label=[]
for line in csv.reader(fp):
    test_raw.append(line)
    test.append(featurize(line,header_2))
    test_label.append(int(line[header_2['WnvPresent']]))
fp.close()

logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(train,train_label)
Z=logreg.predict_proba(test)
Z1=[]

my_data=[]
for x in zip(Z,test_label):
    my_data.append((x[0][1],x[1]))
    Z1.append(x[0][1])
    

print "Logistic Regression Classifier"
print "AUC",  roc_auc_score(test_label,Z1)

