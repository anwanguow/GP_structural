#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import MDAnalysis as md

# Please configure the relevant variables and paths yourself before use.

t_R = 20 # t_{R/2} in the article

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

for num in range(10):
    source = "traj/T_" + str(int(num)) + "/"
    traj_file = source + "traj_unwrap.dcd"
    u = md.lib.formats.libdcd.DCDFile(traj_file)
    N_frame = u.n_frames
    n_atom = u.header['natoms']
    traj = u.readframes()[0]
    
    # t represents the t-th frame in the trajectory file (in DCD format).
    for t in t_set:
        N_mols = len(traj[0])

        p_hop_i = np.zeros((N_mols), dtype = "float32")

        A = np.zeros((t_R+1), dtype = "int")
        B = np.zeros((t_R+1), dtype = "int")

        for i in range(t_R+1):
            A[i] = t-t_R+i
            B[i] = t+i

        r_avg_A = 0
        for i in range(t_R+1):
            r_avg_A = r_avg_A + traj[A[i]]
        r_avg_A = r_avg_A/(t_R+1)

        r_avg_B = 0
        for i in range(t_R+1):
            r_avg_B = r_avg_B + traj[B[i]]
        r_avg_B = r_avg_B/(t_R+1)

        r_sqr_A = 0
        for i in range(t_R+1):
            m_vec = traj[A[i]] - r_avg_B
            sum_sqr = np.power(np.linalg.norm(m_vec, axis = 1),2)
            r_sqr_A = r_sqr_A + sum_sqr
        r_sqr_A = r_sqr_A/(t_R+1)

        r_sqr_B = 0
        for i in range(t_R+1):
            m_vec = traj[B[i]] - r_avg_A
            sum_sqr = np.power(np.linalg.norm(m_vec, axis = 1),2)
            r_sqr_B = r_sqr_B + sum_sqr
        r_sqr_B = r_sqr_B/(t_R+1)
            
        p_hop_i = np.sqrt(r_sqr_A * r_sqr_B)

        np.save("data/D_" + str(int(num)) + "/P_hop_" + str(int(t)) + ".npy", p_hop_i, allow_pickle=True)

    
    
    