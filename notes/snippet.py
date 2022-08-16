# %%
# load modules
from os import P_PIDFD
from tkinter import N
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# %%

N = np.random.normal(loc=10, scale=10, size=10000) 
P = np.random.poisson(lam=10, size=10000) 

# %%
# plot histogram

fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)
ax.hist(N, color='red')
ax.set_ylabel('Count')
ax.set_xlabel('Value')
plt.title('Normal distribution data')
plt.grid(True)
plt.savefig(
    "norm.pgf",
    transparent=True,
    bbox_inches="tight",
    pad_inches=0,
)
# %%
P_FR = Counter(P)
fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)
ax.scatter(P_FR.keys(), P_FR.values(), color='blue')
ax.set_ylabel('Count')
ax.set_xlabel('Value')
plt.title('Poisson distribution data')
plt.grid(True)
plt.savefig(
    "poisson.pgf",
    transparent=True,
    bbox_inches="tight",
    pad_inches=0,
)
# %%
