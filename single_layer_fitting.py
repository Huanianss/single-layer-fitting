import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import psomain
#  python pyinstaller -F -w -i sl1.ico .py
# D:\untitled\substrate_fitting
def test1():
    plt.close('all')
    sizepop = int(pso_sizepop.get())
    maxg = int(pso_maxg.get())
    step = float(pso_step.get())
    step1 = int(data_step.get())
    popmax = [float(max_a.get()), float(max_b.get()), float(max_c.get())]
    popmin = [float(min_a.get()), float(min_b.get()), float(min_c.get())]
    psomain.pso_main(sizepop,maxg,step,step1,popmax,popmin)
    # print(sizepop,maxg,step,'\n',popmax,'\n',popmin)
def test2():
    plt.close('all')
    sizepop = int(pso_sizepop_sl.get())
    maxg = int(pso_maxg_sl.get())
    step = float(pso_step_sl.get())
    step1 = int(data_step_sl.get())
    popmax = [float(max_a_sl.get()), float(max_b_sl.get()), float(max_c_sl.get()), float(max_k0_sl.get()), float(max_k1_sl.get()), float(max_d_sl.get())]
    popmin = [float(min_a_sl.get()), float(min_b_sl.get()), float(min_c_sl.get()), float(min_k0_sl.get()), float(min_k1_sl.get()), float(min_d_sl.get())]
    psomain.pso_main_sl(sizepop,maxg,step,step1,popmax,popmin)
    # print(sizepop,maxg,step,step1,popmax,popmin)

# def change_schedule(now_schedule, all_schedule):
#     canvas.coords(fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 100, 25))
#     root.update()
#     x.set(str(round(now_schedule / all_schedule * 100, 2)) + '%')
#     if round(now_schedule / all_schedule * 100, 2) == 100.00:
#         x.set("完成")
#
root = Tk()
root.title('基板/单层膜折射率拟合 v1.0')
# frame = Frame(root).grid(row=12, column=1)  # 使用时将框架根据情况选择新的位置
# canvas = Canvas(frame, width=120, height=30, bg="white")
# canvas.grid(row=12, column=1)
# x = StringVar()
# # 进度条以及完成程度
# out_rec = canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
# fill_rec = canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="blue")
# Label(frame, textvariable=x).grid(row=12, column=2)


#
Label(root, text='PSO拟合基板参数设置：').grid(row=0, column=0)
Label(root, text='种群规模：').grid(row=1, column=0)
Label(root, text='迭代次数：').grid(row=2, column=0)
Label(root, text='优化算法步长：').grid(row=3, column=0)

Label(root, text='数据间隔:').grid(row=4, column=0)
Label(root, text='柯西公式系数上限：').grid(row=5, column=0)
Label(root, text='a').grid(row=5, column=1)
Label(root, text='b').grid(row=6, column=1)
Label(root, text='c').grid(row=7, column=1)

Label(root, text='柯西公式系数下限：').grid(row=8, column=0)
Label(root, text='a').grid(row=8, column=1)
Label(root, text='b').grid(row=9, column=1)
Label(root, text='c').grid(row=10, column=1)
Label(root, text='使用说明：(不考虑基板吸收，已考虑基板背面反射)').grid(row=12, column=0,columnspan=1)
Label(root, text='1.本程序与包含基板/单层膜0°透过率的“substrate.csv/singleLayer.csv”放置于同一文件夹下').grid(row=13, column=0,columnspan=4)
Label(root, text='2.透过率数据第一列为波长(nm)第二列为透过率(%),数据文件不包含列名').grid(row=14, column=0,columnspan=3)
Label(root, text='3.适当设置以上优化参数及柯西色散公式系数即可导出拟合得折射率数据').grid(row=15, column=0,columnspan=3)
Label(root, text='4.导出的基板折射率“substrate_index.csv”第一行为波长(nm) 第二行为折射率 第三行为柯西公式系数a/b/c').grid(row=16, column=0,columnspan=5)
Label(root, text='5.导出的单层膜折射率“singleLayer_index.csv”第一行为波长(nm) 第二行为折射率 第三行为柯西公式系数a/b/c/k0/k1以及薄膜物理厚度d(nm)').grid(row=17, column=0,columnspan=6)
pso_sizepop = Entry(root)
pso_sizepop.grid(row=1, column=2)
pso_sizepop.insert(0, '20')
pso_maxg = Entry(root)
pso_maxg.grid(row=2, column=2)
pso_maxg.insert(0, '200')
pso_step = Entry(root)
pso_step.grid(row=3, column=2)
pso_step.insert(0, '0.001')

data_step = Entry(root)
data_step.grid(row=4, column=2)
data_step.insert(0, '20')

max_a = Entry(root)
max_a .grid(row=5, column=2)
max_a .insert(0, '2')
max_b = Entry(root)
max_b .grid(row=6, column=2)
max_b .insert(0, '1e5')
max_c = Entry(root)
max_c .grid(row=7, column=2)
max_c .insert(0, '3e8')

min_a = Entry(root)
min_a .grid(row=8, column=2)
min_a .insert(0, '1')
min_b = Entry(root)
min_b .grid(row=9, column=2)
min_b .insert(0, '1e3')
min_c = Entry(root)
min_c .grid(row=10, column=2)
min_c .insert(0, '-3e8')

Button(root, text='1 拟合基板', command=test1).grid(row=11, column=0, columnspan=1)
#

## single layer part
bias=4
Label(root, text='PSO拟合单层膜参数设置：').grid(row=0, column=0+bias)
Label(root, text='种群规模：').grid(row=1, column=0+bias)
Label(root, text='迭代次数：').grid(row=2, column=0+bias)
Label(root, text='优化算法步长：').grid(row=3, column=0+bias)

Label(root, text='数据间隔:').grid(row=4, column=0+bias)
Label(root, text='柯西公式系数上限：').grid(row=5, column=0+bias)
Label(root, text='a').grid(row=5, column=1+bias)
Label(root, text='b').grid(row=6, column=1+bias)
Label(root, text='c').grid(row=7, column=1+bias)
Label(root, text='k0').grid(row=8, column=1+bias)
Label(root, text='k1').grid(row=9, column=1+bias)

Label(root, text='柯西公式系数下限：').grid(row=10, column=0+bias)
Label(root, text='a').grid(row=10, column=1+bias)
Label(root, text='b').grid(row=11, column=1+bias)
Label(root, text='c').grid(row=12, column=1+bias)
Label(root, text='k0').grid(row=13, column=1+bias)
Label(root, text='k1').grid(row=14, column=1+bias)
Label(root, text='物理厚度d上限/nm').grid(row=15, column=1+bias)
Label(root, text='物理厚度d下限/nm').grid(row=16, column=1+bias)

pso_sizepop_sl = Entry(root)
pso_sizepop_sl.grid(row=1, column=2+bias)
pso_sizepop_sl.insert(0, '20')
pso_maxg_sl = Entry(root)
pso_maxg_sl.grid(row=2, column=2+bias)
pso_maxg_sl.insert(0, '200')
pso_step_sl = Entry(root)
pso_step_sl.grid(row=3, column=2+bias)
pso_step_sl.insert(0, '0.001')

data_step_sl = Entry(root)
data_step_sl.grid(row=4, column=2+bias)
data_step_sl.insert(0, '20')

max_a_sl = Entry(root)
max_a_sl .grid(row=5, column=2+bias)
max_a_sl .insert(0, '2')
max_b_sl = Entry(root)
max_b_sl .grid(row=6, column=2+bias)
max_b_sl .insert(0, '1e5')
max_c_sl = Entry(root)
max_c_sl .grid(row=7, column=2+bias)
max_c_sl .insert(0, '3e8')
max_k0_sl = Entry(root)
max_k0_sl .grid(row=8, column=2+bias)
max_k0_sl .insert(0, '0.01')
max_k1_sl = Entry(root)
max_k1_sl .grid(row=9, column=2+bias)
max_k1_sl .insert(0, '1e3')


min_a_sl = Entry(root)
min_a_sl .grid(row=10, column=2+bias)
min_a_sl .insert(0, '1')
min_b_sl = Entry(root)
min_b_sl .grid(row=11, column=2+bias)
min_b_sl .insert(0, '1e3')
min_c_sl = Entry(root)
min_c_sl .grid(row=12, column=2+bias)
min_c_sl .insert(0, '-3e8')
min_k0_sl = Entry(root)
min_k0_sl .grid(row=13, column=2+bias)
min_k0_sl .insert(0, '0')
min_k1_sl = Entry(root)
min_k1_sl .grid(row=14, column=2+bias)
min_k1_sl .insert(0, '0')

max_d_sl = Entry(root)
max_d_sl .grid(row=15, column=2+bias)
max_d_sl .insert(0, '1000')
min_d_sl = Entry(root)
min_d_sl .grid(row=16, column=2+bias)
min_d_sl .insert(0, '1')

Button(root, text='2 拟合单层膜', command=test2).grid(row=14, column=bias, columnspan=1)
# 启动事件循环
root.mainloop()
