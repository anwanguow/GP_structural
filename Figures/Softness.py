#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fig.13(b)
set_ = 2  # Number of set (can be 1 or 2)

select = 5
num = 10
parameter = np.zeros((num), dtype="object")
f = np.zeros((num), dtype="object")
gap = 10
T_min = 100
T_max = 900 + gap
sep = int(np.floor((T_max - T_min) / gap))
T = np.zeros(sep, dtype=np.float32)
for i in range(sep):
    T[i] = T_min + gap * i
x = T
plt.figure(figsize=[5.2, 8])

for i in range(num):
    file = f"results/softness_{int(set_)}/ans_{int(select)}_t_{i}.csv"
    y = pd.read_csv(file, header=None).values.T
    f[i], = plt.plot(x, y)

plt.axhline(y=0, color='r', linestyle='--')
labels = [f"Traj$(T^{{({set_})}}_{{{i+1}}})$" for i in range(num)]
plt.legend(handles=list(f), labels=labels, loc="best", ncol=3)
plt.title("Average Softness")
plt.xlabel("Time $100\\times(0.2\\times(m\\sigma^2/\\epsilon)^{1/2})$")
plt.ylabel("Average Softness, $\\mathfrak{S}(t)$")
plt.show()
