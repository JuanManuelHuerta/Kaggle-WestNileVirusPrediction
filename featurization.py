import sys


f_dict={'Species':{"CULEX PIPIENS":0,"CULEX PIPIENS/RESTUANS":1,"CULEX RESTUANS":2,"CULEX SALINARIUS":3,"CULEX TARSALIS":3,"CULEX TERRITANS":3}}
d_dict={'month':{'01':0,'02':1,'03':2,'04':3,'05':4,'06':5,'07':6,'08':7,'09':8,'10':9,'11':10,'12':11}}
'''
def featurize(l,h,d):
    v=[0.0]*4
    for line in f_matrix:
        if l[h[line[0]]]==line[1]:
            v[line[2]]=1.0
    v2=[0.0]*12
    for line in d_matrix:
        if  d[line[0]]==line[1]:
            v2[line[2]]=1.0
    return v+v2
'''
def featurize(l,h,d):
    v=[0.0]*4
    v2=[0.0]*12
    for vv in f_dict:
        try:
            v[f_dict[vv][l[h[vv]]]]=1.0
        except:
            v[-1]=1.0
    for vv in d_dict:
        try:
            v2[d_dict[vv][d[vv]]]=1.0
        except:
            v2[-1]=1.0

    return v+v2

