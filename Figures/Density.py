#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import linecache as lc

set_index = 1
# Set this value equals 1 for Fig.4(a) and 2 for Fig.15(a)

num = 10
N_frame = 1001

set_name = f"results/Set_{set_index}"
N = np.arange(1, N_frame+1, dtype=int)

lines = []

plt.figure(figsize=[6,10])

for i in range(num):
    logfile = f"{set_name}/T_{i}/nuc.log"
    density = np.zeros(N_frame, dtype=np.float32)
    for j in range(N_frame):
        fields = lc.getline(logfile, 311 + j).split()
        val = fields[9]
        density[j] = 1.0 if val == "-1e+20" else float(val)
    line, = plt.plot(N, density)
    lines.append(line)

plt.xlabel(r"Time $100\,(0.2\,(m\sigma^2/\epsilon)^{1/2})$")
plt.ylabel("Density")
plt.xlim(100, 900)

labels = [
    rf"Traj$(T^{{({set_index})}}_{{{k+1}}})$"
    for k in range(num)
]
plt.legend(handles=lines, labels=labels, loc="best", ncol=4)

plt.title("Density")
plt.tight_layout()
plt.show()
