#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import MDAnalysis as md
from p_hop import p_hop

# Please configure the relevant variables and paths yourself before use.

p_c = 0.1 # p_c in the article

t_R_2 = 20 # t_{R/2} in the article
t_R = 2 * t_R_2

t_set = np.array([100,200,300,400,500,600,700,800,900])

# t_0 represents the t-th frame in the trajectory file (in DCD format).
for t_0 in t_set:
    T = np.zeros((t_R), dtype = "int")
    for i in range(len(T)):
        T[i] = t_0 + i

    for num in range(10):
        source = "traj/T_" + str(int(num)) + "/"
        traj_file = source + "traj_unwrap.dcd"
        u = md.lib.formats.libdcd.DCDFile(traj_file)
        N_frame = u.n_frames
        n_atom = u.header['natoms']
        traj = u.readframes()[0]
        
        hardsoft = np.zeros((len(traj[0])), dtype = "int")

        p_list = np.zeros((len(traj[0]), len(T)), dtype = "float32")

        for t in range(len(T)):
            col = p_list[:,t]
            col[:] = p_hop(traj, T[t], t_R_2)

        for i in range(len(hardsoft)):
            for j in range(len(T)):
                if p_list[i][j] > p_c:
                    hardsoft[i] = 1

        np.save("/storage/mssnkt_grp/msrgxt/new_little/data/D_" + str(int(num)) + "/Y_" + str(int(t_0)) + ".npy", hardsoft, allow_pickle=True)
    
    print(int(t_0))
