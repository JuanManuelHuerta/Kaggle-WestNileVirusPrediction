import sys
import numpy as np
import csv
import datetime


'''
This script is just to get the ball rolling in terms or reading the csv data
'''


#fp=open('../input/train.csv','rt')
#h=fp.readline()
#print h
#for line in csv.reader(fp):
#    print line
#fp.close()

#"Station","Date","Tmax","Tmin","Tavg","Depart","DewPoint","WetBulb","Heat","Cool","Sunrise","Sunset","CodeSum","Depth","Water1","SnowFall","PrecipTotal","StnPressure","SeaLevel","ResultSpeed","ResultDir","AvgSpeed"

fp=open('../input/weather.csv','rt')
h=fp.readline().rstrip().replace("\"","").split(",")
print h
for line in csv.reader(fp):
    print line
fp.close()



