#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from features import F_Psi_with_cut
import MDAnalysis as md
from sklearn.preprocessing import normalize

# Please configure the relevant variables and paths yourself before use.

# t represents the t-th frame in the trajectory file (in DCD format).
t_set = np.array([100,200,300,400,500,600,700,800,900])
num = np.array([0,1,2,3,4,5,6,7,8,9])
# num is the number of trajectory (starting from 0), and the range is 0 to 9.

for number in num:
    source = "traj/T_" + str(int(number)) + "/"
    traj_file = source + "traj.dcd"
    u = md.lib.formats.libdcd.DCDFile(traj_file)
    N_frame = u.n_frames
    n_atom = u.header['natoms']
    traj = u.readframes()[0]

    for t in t_set:
        pos = traj[int(t)]
        N = len(pos)
        Dt = np.load('distance_table/D_' + str(int(number)) + '/D_' + str(int(t)) + '.npy', allow_pickle=True)
        data = np.zeros((N, 20), dtype = "float32")
        
        for j in range(N):
            # idx, env, xi, zeta, lambda_, table, r_cut
            data[j,0] = F_Psi_with_cut(j, pos, 3.5, 1, -1, Dt, 4)
            data[j,1] = F_Psi_with_cut(j, pos, 3.5, 1, 1, Dt, 4)
            data[j,2] = F_Psi_with_cut(j, pos, 3.5, 2, -1, Dt, 4)
            data[j,3] = F_Psi_with_cut(j, pos, 3.5, 2, 1, Dt, 4)
            data[j,4] = F_Psi_with_cut(j, pos, 3.5, 4, 1, Dt, 4)
            data[j,5] = F_Psi_with_cut(j, pos, 3.0, 1, 1, Dt, 4)
            data[j,6] = F_Psi_with_cut(j, pos, 3.0, 2, 1, Dt, 4)
            data[j,7] = F_Psi_with_cut(j, pos, 3.0, 4, 1, Dt, 4)
            data[j,8] = F_Psi_with_cut(j, pos, 2.5, 1, 1, Dt, 4)
            data[j,9] = F_Psi_with_cut(j, pos, 2.5, 2, 1, Dt, 4)
            data[j,10] = F_Psi_with_cut(j, pos, 2.5, 4, 1, Dt, 4)
            data[j,11] = F_Psi_with_cut(j, pos, 2.0, 1, 1, Dt, 4)
            data[j,12] = F_Psi_with_cut(j, pos, 2.0, 2, 1, Dt, 4)
            data[j,13] = F_Psi_with_cut(j, pos, 2.0, 4, 1, Dt, 4)
            data[j,14] = F_Psi_with_cut(j, pos, 1.6, 1, 1, Dt, 4)
            data[j,15] = F_Psi_with_cut(j, pos, 1.6, 2, 1, Dt, 4)
            data[j,16] = F_Psi_with_cut(j, pos, 1.6, 4, 1, Dt, 4)
            data[j,17] = F_Psi_with_cut(j, pos, 1, 1, 1, Dt, 4)
            data[j,18] = F_Psi_with_cut(j, pos, 1, 2, 1, Dt, 4)
            data[j,19] = F_Psi_with_cut(j, pos, 1, 4, 1, Dt, 4)
            print(t,"_",j)
        data = normalize(data, axis=0, norm='max')
        np.save("data/D_" + str(int(number))  + "/B_" + str(int(t)) + ".npy", data, allow_pickle=True)

