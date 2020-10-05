#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    basic_array_methods.py  |  ndarray, the fundamental NumPy object
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + what's special in NumPy?
    + ndarrays
    + basic methods
    + universal functions

"""

# %% what's special in NumPy?

"""
1. NumPy is efficient! The library has been built such that users don't
   need for loops!!

2. ...it's flexible

3. ...it integrates seamlessly with SciPy

4. ...and it goes very well with Numba
"""

# %% ndarrays

"""
ndarrays support vectorization: a single operation can be carried out on
an entire array, rather than requiring an explicit loop over the array’s elements (Hill, 2015)
"""

# loding NumPy
import numpy as np

# initializing ndarrays
# --+ alternative 1 - calling the np.array constructor
a = np.array((100, 101, 102, 103))
a

b = np.array([[1.,2.], [3.,4.]])
b

# --+ alternative 2 - special cases
"""
np.empty, takes a tuple of the array’s shape and creates the array without
initializing its elements; initial elements are undefined (Hill, 2015)
"""
np.empty((2,2))

"""
np.zeros creates arrays whose elements are prefilled with 0s
"""
np.zeros((3,2))

"""
np.ones creates arrays whose elements are prefilled with 1s
"""
np.ones((3,2))

# --+ alternative 3 - using a numerical sequence
np.arange(10)
np.linspace(1, 10, 10)

# --+ alternative 4 - initializing from a function
def f(i, j):
    return 2 * i * j

np.fromfunction(f, (4,3))

# %% basic methods for ndarrays
a = np.array(((1, 0, 1), (0, 1, 0)))

"""
The array dimensions: the size of the array along each of its axes, returned
as a tuple of integers
"""
a.shape

"""
The total number of elements in the array, equal to the product of the
elements of shape
"""
a.size

"""
Number of axes (dimensions). Note that ndim == len(shape)
"""
a.ndim

"""
The array’s data type (see Section 6.1.2)
"""
a.dtype

# %% universal functions

# sample arrays
x = np.linspace(1,5,5)
y = np.exp(-np.linspace(0., 2., 5))

# the math module provides plenty of functions
np.sqrt(x - 1)
np.sin(x - y)
