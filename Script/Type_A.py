#!/usr/bin/env python39
# -*- coding: utf-8 -*-

import numpy as np
from features import F_G
import MDAnalysis as md
from sklearn.preprocessing import normalize

# Please configure the relevant variables and paths yourself before use.

gap = 100
T_min = 100
T_max = 900+gap
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype = "float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i-1] + gap
T = T.astype(np.float32)
t_set = T
# t represents the t-th frame in the trajectory file (in DCD format).

NN = np.array([0])

for number in NN:
    source = "traj/T_" + str(int(number)) + "/"
    traj_file = source + "traj.dcd"
    u = md.lib.formats.libdcd.DCDFile(traj_file)
    N_frame = u.n_frames
    n_atom = u.header['natoms']
    traj = u.readframes()[0]

    for t in t_set:
        # gap represents \delta of Type A (G function) in the article.
        gap = 0.1
        # T_min represents r_0
        T_min = 1
        # T_max represents r_max
        T_max = 7+gap
        # The gap parameter is used to address rounding issues.
        # Please test whether your range and interval settings require adding a gap.
        sep = np.floor((T_max - T_min) / gap).astype(np.int16)
        T = np.zeros(sep, dtype = "float64")
        T[0] = T_min
        T[1] = T_min + gap
        for i in range(2, sep):
            T[i] = T[i-1] + gap
        T = T.astype(np.float32)
        
        N = len(traj[0])
        features = sep

        Dt = np.load('distance_table/D_' + str(int(number)) + '/D_' + str(int(t)) + '.npy', allow_pickle=True)
        data = np.zeros((N, features), dtype = "float32")

        for i in range(features):
            for j in range(N):
                data[j,i] = F_G(j, Dt, T[i], 0.1)
            print(i)

        data = normalize(data, axis=0, norm='max')
        np.save("data/D_" + str(int(number)) + "/A_" + str(int(t)) + ".npy", data, allow_pickle=True)
        print(number, "_", t)
