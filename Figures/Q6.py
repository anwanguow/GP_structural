#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

set_index = 1
# Set this value equals 1 for Fig.3(b) and 2 for Fig.14(b)

num = 10
set_name = f"results/Set_{set_index}"
N_frame = 1001
N = np.arange(1, N_frame+1, dtype=int)

lines = []

plt.figure(figsize=(5,8))

for i in range(num):
    logfile = f"{set_name}/T_{i}/nuc.log"
    v_max_n = np.zeros(N_frame, dtype=int)
    for j in range(N_frame):
        txt = lc.getline(logfile, 311 + j).split()
        val = txt[6]
        v_max_n[j] = 1 if val == "-1e+20" else int(val)
    line, = plt.plot(N, v_max_n)
    lines.append(line)

plt.xlabel(r"Time $100\,(0.2\,(m\sigma^2/\epsilon)^{1/2})$")
plt.ylabel(r"Global bond order parameter $Q_6$")
plt.title(r"Global bond order parameter $Q_6$")
plt.xlim(100, 900)

labels = [
    rf"Traj$(T^{{({set_index})}}_{{{k+1}}})$"
    for k in range(num)
]
plt.legend(handles=lines, labels=labels, loc="best")

plt.tight_layout()
plt.show()
