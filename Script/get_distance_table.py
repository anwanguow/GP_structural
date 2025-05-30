#!/usr/bin/env python39
# -*- coding: utf-8 -*-

import numpy as np
import MDAnalysis as md

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

        Dt = np.zeros((len(pos), len(pos)), dtype = "float32")

        for i in range(len(pos)-1):
            vec_i = pos[i]
            for j in range(i+1, len(pos)):
                vec_j = pos[j]
                vec_ij = vec_i - vec_j
                Dt[i,j] = np.sqrt(np.power(vec_ij[0],2) + np.power(vec_ij[1],2) + np.power(vec_ij[2],2))

        Dt = Dt + np.transpose(Dt)
        np.save('distance_table/D_' + str(int(number)) + '/D_' + str(int(t)), Dt, allow_pickle=True)
        print(number, "-", int(t))


