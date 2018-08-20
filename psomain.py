import time
# import random
import numpy as np
# from MF import fun
# import slf
import miritFunc
import copy
import matplotlib.pyplot as plt
##
import csv
def pso_main(sizepop,maxg,step,step1,popmax,popmin):
    a = csv.reader(open('substrate.csv'))
    a = np.array(list(a),dtype='float64')

    tic = time.time()
    c1 = 1.49445
    c2 = 1.49445
    # maxg = 200 # 迭代次数
    # sizepop = 20 # 种群规模

    paranum = len(popmax) # 参数个数
    yy = np.ones([maxg,1])
    # Vmax=1
    # Vmin=-1
    # popmax = [2 ,1e7]
    # popmin = [1 ,0]
    pop = np.ones([sizepop, paranum])
    # print(pop)
    V = np.ones([sizepop, paranum])
    # print(V)
    fitness = np.ones(sizepop)
    for i in range(sizepop):
        for j in range(paranum):
            pop[i,j] = np.random.random()*(popmax[j]-popmin[j])+popmin[j]
        # pop[i,:]= np.random.random([1,paranum])
        # V[i,:] = np.random.random([1,paranum])
        V[i, :] = pop[i,:]
        y,t=miritFunc.fun(pop[i,:],step1,a)
        fitness[i]=y
    # print(type(fitness))
    bestfitness = np.min(fitness)
    bestindex = np.where(fitness == np.min(fitness))[0][0]
    # [bestfitness,bestindex]=min(fitness)
    zbest = copy.deepcopy(pop[bestindex,:])
    gbest = pop
    fitnessgbest = fitness
    fitnesszbest = bestfitness
    # print(pop,bestfitness, bestindex,zbest,gbest,fitnessgbest,fitnesszbest)
    # print('-----------------------------------------')
    ##
    lam = (a[0::step1, 0])
    sub = (a[0::step1, 1])
    fig = plt.figure('拟合情况')
    ax = fig.add_subplot(1,1,1)
    ax.scatter(lam, sub)
    plt.xlabel('lambda/nm')
    plt.ylabel('T/%')
    plt.ion()
    plt.show()
    ##
    for i in range(maxg):
        for j in range(sizepop):
            V[j,:] = V[j,:] + c1 * np.random.random() * (gbest[j,:] - pop[j,:]) + c2 * np.random.random() * (zbest - pop[j,:])
            # np.minimum(V,Vmax)
            # np.maximum(V, Vmax)
            pop[j,:]=pop[j,:]+step* V[j,:]
            if (pop[j, 0] > popmax[0]): pop[j, 0] =popmax[0]
            if (pop[j, 1] > popmax[1]): pop[j, 1]=popmax[1]
            if (pop[j, 2] > popmax[2]): pop[j, 2] = popmax[2]
            #
            if (pop[j, 0] < popmin[0]): pop[j, 0] = popmin[0]
            if (pop[j, 1] < popmin[1]) :pop[j, 1] = popmin[1]
            if (pop[j, 2] < popmin[2]): pop[j, 2] = popmin[2]

            # 自适应变异
            if(np.random.random()>0.8):
                k = int(np.random.random()*paranum)
                pop[j, k] = np.random.random()*(popmax[k]-popmin[k])+popmin[k]
            #     适应度值
            # fitness[j] = fun(pop[j,:])
            y, t= miritFunc.fun(pop[j, :],step1,a)
            fitness[j]=y
            if fitness[j] < fitnessgbest[j]:
                gbest[j, :] = pop[j, :]
                fitnessgbest[j] = fitness[j]

            if fitness[j] < fitnesszbest:
                zbest = copy.deepcopy(pop[j, :])
                fitnesszbest = fitness[j]
        yy[i] = fitnesszbest
        if i%(int(maxg/20))==0:
            print(i)
            # slf.change_schedule(int(i/maxg), 99)
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            # plot the prediction
            y, t= miritFunc.fun(zbest,step1,a)
            lines = ax.plot(lam, t , 'r-', lw=2)
            plt.pause(0.01)
    plt.ioff()
    toc = time.time()

    print('最优值：', zbest)

    print('MF:', fitnesszbest)
    # print(fun(zbest))
    print('time:', toc-tic)
    # print(yy)
    # print(bestindex)
    plt.figure('评价函数')
    plt.plot(range(maxg),yy)
    plt.xlabel('Iteration')
    plt.ylabel('RMS')
    plt.figure('基板折射率')
    plt.plot(lam,zbest[0]+zbest[1]/lam**2+zbest[2]/lam**4)
    plt.xlabel('lambda/nm')
    plt.ylabel('n')
    n_sub=zbest[0]+zbest[1]/lam**2+zbest[2]/lam**4
    with open('substrate_index.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for list1 in lam,n_sub:
            csv_writer.writerow(list1)
        csv_writer.writerow(zbest)
    plt.show()
def pso_main_sl(sizepop,maxg,step,step1,popmax,popmin):
    a = csv.reader(open('singleLayer.csv'))
    a = np.array(list(a),dtype='float64')
    lam = (a[0::step1, 0])
    sub = (a[0::step1, 1])
    subs = csv.reader(open('substrate.csv'))
    subs = np.array(list(subs), dtype='float64')
    b = csv.reader(open('substrate_index.csv'))
    b = np.array(list(b)[2], dtype='float64')

    tic = time.time()
    c1 = 1.49445
    c2 = 1.49445
    # maxg = 200 # 迭代次数
    # sizepop = 20 # 种群规模

    paranum = len(popmax) # 参数个数
    yy = np.ones([maxg,1])
    # Vmax=1
    # Vmin=-1
    # popmax = [2 ,1e7]
    # popmin = [1 ,0]
    pop = np.ones([sizepop, paranum])
    # print(pop)
    V = np.ones([sizepop, paranum])
    # print(V)
    fitness = np.ones(sizepop)
    for i in range(sizepop):
        for j in range(paranum):
            pop[i,j] = np.random.random()*(popmax[j]-popmin[j])+popmin[j]
        # pop[i,:]= np.random.random([1,paranum])
        V[i,:] = np.random.random([1,paranum])
        # V[i, :] = pop[i,:]
        y,t=miritFunc.fun_sl(pop[i,:],step1,a,b)
        fitness[i]=y
    # print(type(fitness))
    bestfitness = np.min(fitness)
    bestindex = np.where(fitness == np.min(fitness))[0][0]
    # [bestfitness,bestindex]=min(fitness)
    zbest = copy.deepcopy(pop[bestindex,:])
    gbest = pop
    fitnessgbest = fitness
    fitnesszbest = bestfitness
    # print(pop,bestfitness, bestindex,zbest,gbest,fitnessgbest,fitnesszbest)
    # print('-----------------------------------------')
    ##

    fig = plt.figure('拟合情况')
    ax = fig.add_subplot(1,1,1)
    ax.scatter(lam, sub)
    ax.scatter(subs[0::step1, 0],subs[0::step1, 1])
    plt.xlabel('lambda/nm')
    plt.ylabel('T/%')
    plt.ion()
    plt.show()
    ##
    for i in range(maxg):
        for j in range(sizepop):
            V[j,:] = V[j,:] + c1 * np.random.random() * (gbest[j,:] - pop[j,:]) + c2 * np.random.random() * (zbest - pop[j,:])
            # np.minimum(V,Vmax)
            # np.maximum(V, Vmax)
            pop[j,:]=pop[j,:]+step* V[j,:]
            if (pop[j, 0] > popmax[0]):pop[j, 0] = popmax[0]
            if (pop[j, 1] > popmax[1]): pop[j, 1] = popmax[1]
            if (pop[j, 2] > popmax[2]): pop[j, 2] = popmax[2]
            if (pop[j, 3] > popmax[3]): pop[j, 3]= popmax[3]
            if (pop[j, 4] > popmax[4]): pop[j, 4] = popmax[4]
            if (pop[j, 5] > popmax[5]): pop[j, 5] = popmax[5]
            #
            if (pop[j, 0] < popmin[0]): pop[j, 0]=popmin[0]
            if (pop[j, 1] < popmin[1]) :pop[j, 1]=popmin[1]
            if (pop[j, 2] < popmin[2]): pop[j, 2] = popmin[2]
            if (pop[j, 3] < popmin[3]) :pop[j, 3]=popmin[3]
            if (pop[j, 4] < popmin[4]): pop[j, 4] = popmin[4]
            if (pop[j, 5] < popmin[5]): pop[j, 5] = popmin[5]

            # 自适应变异
            if(np.random.random()>0.8):
                k = int(np.random.random()*paranum)
                pop[j, k] = np.random.random()*(popmax[k]-popmin[k])+popmin[k]
            #     适应度值
            # fitness[j] = fun(pop[j,:])
            y, t= miritFunc.fun_sl(pop[j, :],step1,a,b)
            fitness[j]=y
            if fitness[j] < fitnessgbest[j]:
                gbest[j, :] = pop[j, :]
                fitnessgbest[j] = fitness[j]

            if fitness[j] < fitnesszbest:
                zbest = copy.deepcopy(pop[j, :])
                fitnesszbest = fitness[j]
        yy[i] = fitnesszbest
        if i%(int(maxg/20))==0:
            print(i)
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            # plot the prediction
            y, t= miritFunc.fun_sl(zbest,step1,a,b)
            lines = ax.plot(lam, t , 'r-', lw=2)
            plt.pause(0.01)
    plt.ioff()
    toc = time.time()

    print('最优值：', zbest)

    print('MF:', fitnesszbest)
    # print(fun(zbest))
    print('time:', toc-tic)
    # print(yy)
    # print(bestindex)
    plt.figure('评价函数')
    plt.plot(range(maxg),yy)
    plt.xlabel('Iteration')
    plt.ylabel('RMS')
    plt.figure('单层膜折射率')
    plt.plot(lam,zbest[0]+zbest[1]/lam**2+zbest[2]/lam**4)
    plt.xlabel('\lambda/nm')
    plt.ylabel('real(n)')
    n_slayer=zbest[0]+zbest[1]/lam**2+zbest[2]/lam**4
    k_slayer=zbest[3]*np.exp(zbest[4]/lam)

    with open('singleLayer_index.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for list1 in lam,n_slayer,k_slayer:
            csv_writer.writerow(list1)
        csv_writer.writerow(zbest)
    plt.show()






