#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    list_comprehensions.py  |  Control flow, iterators/loops
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + what's a list comprehension
    + examples

"""


# %% what's a list comprehension?

"""
List comprehension Alist comprehension in Python isa construct for creating a
listbased on another iterable object in a single line of code. For example,
given a list of numbers, xlist,alistofthe squares of those numbers may be
generated as follows: This is a faster and syntactically nicer way of creating
the same list with a block of code within a for loop (Hill, 2015).
"""

# backbone of a list comprehension
# --+ we need an iterable object ― e.g., a list of company names
companies = ['Apple', 'Microsoft', 'Lenovo', 'Intel']
# --+ task to repeat: let's print out each company name separately
[company.upper() for company in companies]

# %% examples

# example 1: get the z-scores of an observed distribution
# --+ the distribution
import numpy as np
d = np.random.poisson(lam=6, size=100)
d
# --+ get mean and standard deviation
mu, std = np.mean(d), np.std(d)
# --+ the list comprehension initializes a new object
z = [(i - mu)/std for i in d]
z

# example 2: create all possible permutations involving two sets and store
#            them in a new list
# --+ data
l_0 = [1, 2, 3]
l_1 = ['a', 'b', 'c']
# --+ once again, the list comprehension initializes a new object
output = [[i, j] for i in l_0 for j in l_1]
output

# example 3: match the elements from two lists that occupy the same position
#            (i.e., have same index) and store them in a new list
output = [[i, j] for i, j in zip(l_0, l_1)]
output

# example 2: expand on example 3 by including an arbitrary conditional
#            statement
output = [[i, j] for i in l_0 for j in l_1 if (i > 1) & (j == 'a')]
output
