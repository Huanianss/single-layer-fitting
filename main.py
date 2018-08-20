import numpy as np
import matplotlib.pyplot as plt
import csv
# from calc import ca_r
import math
def calc(n1_0,n1_1,n1_2,lam):
    # n0=1
    ns=n1_0+n1_1/lam**2+n1_2/lam**4
    r1 = ((ns - 1) / (ns+ 1)) ** 2
    rr = r1 + r1 * (1 - r1) ** 2. / (1 - r1 * r1)
    rr = rr * 100
    tt = 100 - rr
    return tt
calc_multi = np.frompyfunc(calc, 4, 1)

def calc_sl(n1_0,n1_1,n1_2,k1_0,k1_1,d,b0,b1,b2,lam):
    n0=1
    # a = csv.reader(open('substrate_index.csv'))
    # a = np.array(list(a)[2], dtype='float64')

    n_sub=b0+b1/lam**2+b2/lam**4

    n_sl = n1_0 + n1_1 / np.square(lam) + n1_2 / np.square(lam) / np.square(lam) - k1_0*np.exp(k1_1/lam)*1j
    delta=2*np.pi/lam*n_sl*d
    y0 = 1 / 120 / math.pi
    ## 求解t12
    yita0=n0*y0
    yita1=n_sl*y0
    yitas=n_sub*y0
    B=np.cos(delta)+yitas/yita1*np.sin(delta)*1j
    C=yitas*np.cos(delta)+yita1*np.sin(delta)*1j
    t12 = np.real(4 * yita0 * yitas / ((yita0 * B + C) * (yita0 * B + C).conjugate()))

    ## 求解r21
    yita0 = n_sub * y0
    yitas = n0 * y0
    B = np.cos(delta) + yitas / yita1 * np.sin(delta) * 1j
    C = yitas * np.cos(delta) + yita1 * np.sin(delta) * 1j
    r1 = (yita0 * B - C) / (yita0 * B + C)
    r21=np.real(r1*r1.conjugate())

    r23 = ((n_sub - 1) / (n_sub+ 1)) ** 2
    tt=100*t12*(1-r23)/(1-r21*r23)
    return tt
calc_multi_sl = np.frompyfunc(calc_sl, 10, 1)



if __name__ == '__main__':

    lam=range(100,1000,1)
    tt=calc_multi(2,1e6,1e11,lam)
    # rr,tt=calcu(n0,ns,d,n_index,lam,theta0,isTM)
    # plt.plot(lam,rr)
    plt.plot(lam,tt)
    # # plt.plot(lam,rr+tt)
    plt.show()
    # print(np.(tt))




