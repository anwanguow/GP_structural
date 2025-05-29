#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fig.13(a)
set_ = 2  # Number of set (can be 1 or 2)

select = 5
num = 10
gap = 10
T_min = 100
T_max = 900 + gap
sep = int((T_max - T_min) / gap)
T = np.linspace(T_min, T_min + (sep - 1) * gap, sep, dtype=np.float32)
x = T
plt.figure(figsize=[5, 8])
lines = []

for i in range(num):
    file_path = f"results/set_{set_}_/ans_{select}_t_{i}.csv"
    y = pd.read_csv(file_path, header=None).values.T
    (line,) = plt.plot(x, y)
    lines.append(line)

labels = [f"Traj$(T^{({set_})}_{{{i}}})$" for i in range(1, num + 1)]
plt.legend(handles=lines, labels=labels, loc="best")
plt.title("Hard Particle Counter")
plt.xlabel(r"Time $100\times(0.2\times(m\sigma^2/\epsilon)^{1/2})$")
plt.ylabel(r"Hard particle counter, $\mathfrak{N}(t)$")
plt.tight_layout()
plt.show()
