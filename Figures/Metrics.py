#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import linecache as lc

# (2, 6) for Fig.9(a)
# (2,7) for Fig.9(b)
set_ = 2 # The number of set
num = 6 # The number of trajectory

N = 864
select = 5
N_frame = 1001;
gap = 10
T_min = 100
T_max = 900+gap
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype = "float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i-1] + gap
T = T.astype(np.float32)
x = T

i = num-1
file_counter = "results/set_" + str(int(set_)) + "_/ans_" + str(int(select)) + "_t_" + str(int(i)) + ".csv"
file_softness = "results/softness_" + str(int(set_)) + "/ans_" + str(int(select)) + "_t_" + str(int(i)) + ".csv"
file_q6msd = ""

if set == 1:
    file_q6msd = "results/Set_1/T_" + str(int(i)) + "/nuc.log"
else:
    file_q6msd = "results/Set_2/T_" + str(int(i)) + "/nuc.log"
    
    
y_0 = pd.read_csv(file_counter, header=None)
y_0 = np.transpose(y_0.values)

y_1 = np.zeros((sep), dtype = "int")
y_2 = np.zeros((sep), dtype = "float64")

y_3 = pd.read_csv(file_softness, header=None)
y_3 = np.transpose(y_3.values)


v_max_1 = np.zeros((N_frame), dtype="int")
v_max_2 = np.zeros((N_frame), dtype="int")
for j in range(N_frame):
    txt = str.split(lc.getline(file_q6msd, 311 + j))
    num_str_1 = txt[6];
    if num_str_1 == "-1e+20":
        v_max_1[j] = 1
    else:
        v_max_1[j] = int(num_str_1)
    
    num_str_2 = txt[3];
    if num_str_2 == "-1e+20":
        v_max_2[j] = 0
    else:
        v_max_2[j] = np.float64(num_str_2)

for j in range(sep):
    idx = 100 + j * 10
    y_1[j] = v_max_1[idx]
    y_2[j] = v_max_2[idx]

plt.figure(figsize=[7,6])
plt.xlabel("Time $100*(0.2*(m*\sigma^2/\epsilon)^{1/2})$")
plt.axhline(y=0, color='r', linestyle='--')
f1 ,= plt.plot(x,y_0/N)
f2 ,= plt.plot(x,y_1/N)
f3 ,= plt.plot(x,y_3)
plt.legend(handles=[f1,f2,f3], labels = ["Normalized Hard particle counter, $\mathfrak{N}(t)/\mathcal{N}$","Normalized $Q_6$ order parameter, $Q_6(t)/\mathcal{N}$", "Average Softness $\mathfrak{S}(t)$"], loc="best")
plt.title("Traj($T^{(" + str(int(set_)) + ")}_" + str(int(num)) + "$)")
