# %%
# load modules
import numpy as np
import matplotlib.pyplot as plt

# %%

x = np.arange(0, 15, 1)
y = [4, 4, 8, 6, 11, 13, 17, 11, 21, 28, 23, 23, 25, 29, 37]
A = np.vstack([x, np.ones(len(x))]).T
A
b = np.linalg.lstsq(A, y,)[0]
b

fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111)
ax.plot(x, y, 'o', label='Observed data', color='gray', markersize=5)
ax.plot(x, b[1]*x + b[0], 'blue', label='OLS estimate')
ax.set_xticks([0, 5, 10, 15])
ax.set_xticklabels(['0', '5', '10', '15'])
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.legend()
plt.grid(True)
plt.savefig(
    "ols.pgf",
    transparent=True,
    bbox_inches="tight",
    pad_inches=0,
)
# %%
