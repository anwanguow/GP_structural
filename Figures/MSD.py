#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

set_index = 1
# Set this value equals 1 for Fig.3(a) and 2 for Fig.14(a)

num = 10
N_frame = 1001

set_name = f"results/Set_{set_index}"
N = np.arange(1, N_frame+1, dtype=int)

lines = []

plt.figure(figsize=(4,8))

for i in range(num):
    logfile = f"{set_name}/T_{i}/nuc.log"
    msd = np.zeros(N_frame, dtype=float)
    for j in range(N_frame):
        fields = lc.getline(logfile, 311 + j).split()
        val = fields[3]
        msd[j] = 0.0 if val == "-1e+20" else float(val)
    line, = plt.plot(N, msd)
    lines.append(line)

plt.xlim(100, 900)
plt.title("Mean Square Displacement (MSD)")
plt.xlabel(r"Time $100\,(0.2\,(m\sigma^2/\epsilon)^{1/2})$")
plt.ylabel("Mean Squared Displacement (MSD)")

labels = [
    rf"Traj$(T^{{({set_index})}}_{{{k+1}}})$"
    for k in range(num)
]
plt.legend(handles=lines, labels=labels, loc="best")

plt.tight_layout()
plt.show()
