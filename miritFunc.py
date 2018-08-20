import csv
import numpy as np
import main
def fun(x,step1,a):
    n1_0=x[0]
    n1_1=x[1]
    n1_2=x[2]
    y=0
    # theta0=0
    # a = csv.reader(open('substrate.csv'))
    # a = np.array(list(a),dtype='float64')
    # len_l=np.shape(a)[0]
    # step1=30
    # t=np.ones([len_l])
    # for i in range(0,len_l,step1):
    lam = (a[0::step1, 0])
    sub = (a[0::step1, 1])
    tt=main.calc_multi(n1_0,n1_1,n1_2,lam)
        # tt=main.main(n1_0,n1_1,lam)
        # t[i]=tt
    y=np.sqrt(np.mean(np.square(abs(sub-tt))))
    # y=y/np.shape(a)[0]
    return y,tt
def fun_sl(x,step1,a,b):
    n1_0=x[0]
    n1_1=x[1]
    n1_2=x[2]
    k1_0=x[3]
    k1_1=x[4]
    d = x[5]
    y=0
    # theta0=0
    # a = csv.reader(open('singleLayer.csv'))  #单层膜透过率
    # a = np.array(list(a),dtype='float64')
    # b = csv.reader(open('substrate_index.csv'))
    # b = np.array(list(b)[2], dtype='float64')
    # a=0
    # b=[0,0,0]
    # len_l=np.shape(a)[0]
    # step1=30
    # t=np.ones([len_l])
    # for i in range(0,len_l,step1):
    lam = (a[0::step1, 0])
    sub = (a[0::step1, 1])
    tt=main.calc_multi_sl(n1_0,n1_1,n1_2,k1_0,k1_1,d,b[0],b[1],b[2],lam)
        # tt=main.main(n1_0,n1_1,lam)
        # t[i]=tt
    y=np.sqrt(np.mean(np.square(abs(sub-tt))))
    # y=y/np.shape(a)[0]
    return y,tt

