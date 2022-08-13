# %%
# load modules
import numpy as np
import matplotlib.pyplot as plt

# %%
X = np.arange(1, 11, 1)
Y = np.arange(10, 0, -1)

X = X.reshape(5, 2)
Y = Y.reshape(5, 2)

np.inner(X, Y)

