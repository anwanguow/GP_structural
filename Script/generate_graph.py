#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import MDAnalysis as md
from p2g import pos2graph

# Please configure the relevant paths yourself before use.

# r_c is the cut-off distance of the modified Voronoi methods.
r_c_arr = np.array([2.5])

gap = 0.01
T_min = 0.51
T_max = 1+gap
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype = "float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i-1] + gap
T = T.astype(np.float32)
f_c_arr = T
# f_c is \mathcal{A} in the article.

gap = 25
T_min = 100
T_max = 900+gap
sep = np.floor((T_max - T_min) / gap).astype(np.int16)
T = np.zeros(sep, dtype = "float64")
T[0] = T_min
T[1] = T_min + gap
for i in range(2, sep):
    T[i] = T[i-1] + gap
T = T.astype(np.float32)
t_arr = T
# t represents the t-th frame in the trajectory file (in DCD format).

p = 0
# p is the number of trajectory (starting from 0), and the range is 0 to 9.

source = "traj/T_" + str(int(p)) + "/"
traj_file = source + "traj.dcd"
u = md.lib.formats.libdcd.DCDFile(traj_file)
N_frame = u.n_frames
n_atom = u.header['natoms']
traj = u.readframes()[0]

for r_c in r_c_arr:
    for f_c in f_c_arr:
        for t in t_arr:
            pos = traj[int(t)]
            A = pos2graph(pos,r_c,f_c)
            data_save = "./graph/D_" + str(int(p)) + "/T_" + str(int(t)) + "_r_" + str(r_c) + "_f_" + str(f_c) + ".npy"
            np.save(data_save, A, allow_pickle=True)
            print(p, "_", f_c, "_", t)

