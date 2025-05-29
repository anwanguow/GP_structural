#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# Please configure the relevant variables and paths yourself before use.

t_arr = np.array([100,200,300,400,500,600,700,800,900])
r_c_arr = np.array([2.5])
f_c_arr = np.array([0.55,0.6,0.65,0.7,0.75])

for p in range(10):
    
    for t in t_arr:
        X = np.zeros((864, 0), dtype = "float32")
        for r_c in r_c_arr:   
            for f_c in f_c_arr:
                M = np.load("./data/D_" + str(int(p)) + "/A_" + str(int(t)) + "_r_" + str(r_c) + "_f_" + str(f_c) + ".npy", allow_pickle=True)
                X = np.column_stack((X, M))
        Psi = np.load("data/D_" + str(int(p))  + "/B_" + str(int(t)) + ".npy", allow_pickle=True)
        Y = np.load("data/D_" + str(int(p)) + "/Y_" + str(int(t)) + ".npy", allow_pickle=True)
        
        Yn = np.zeros((len(Y)), dtype = "int")
        for j in range(len(Yn)):
            if Y[j] == True:
                Yn[j] = 1
            else:
                Yn[j] = 0
        
        A = pd.DataFrame(X)
        C = pd.DataFrame(Psi)
        B = pd.DataFrame(Yn)
        r = pd.concat([A, C], axis=1)
        r = pd.concat([r, B], axis=1)
        r.to_csv("matlab/data/D_" + str(int(p)) + "/mix_graph_0.55_0.6_0.65_0.7_0.75_and_psi_20_" + str(int(t)) + ".csv", index = False, header = False)
        
        print(p, "_" ,t)


