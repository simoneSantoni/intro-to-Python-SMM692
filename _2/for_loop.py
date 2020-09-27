#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    for_loop.py  |  Control flow, iterators/loops
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + what's a for loop?
    + examples

"""

# %% what's a for loop?

"""
It is often necessary to take the items in an iterable object one by one and
do something with each in turn. For example, we may want to transform a list
of company names by removing some accidental leading and trailing blanks.
That's a boaring task we should be better off automating.

Other languages, such as C, require this type of loop to refer to each item in
turn by its integer index. In Python this is possible, but the more natural
and convenient way is with the idiom:

'for item in iterable object:'

"""

# backbone of a foor loop
# --+ we need an iterable object ― e.g., a list of company names
companies = ['Apple', 'Microsoft', 'Lenovo', 'Intel']
# --+ task to repeat: let's print out each company name separately
for company in companies:
    print(company)

# %% examples

# example 1: get the z-scores of an observed distribution
# --+ the distribution
import numpy as np
d = np.random.poisson(lam=6, size=100)
d
# --+ get mean and standard deviation
mu, std = np.mean(d), np.std(d)
# --+ empty container
z = []
for i in d:
    to_append = (i - mu) / std
    z.append(to_append)

z

# example 2: cleaning a list with string data, display the result, and provide
#            details on the counts of changes made on each element of the list
# --+ US cities with leading and trailing blanks
cities = [' New York', 'San Fran', 'Boston ', ' Chicago ']
# --+ let's display the clean string
for city in cities:
    clean_str = city.strip()
    print('''
    -------------------------------
    City: {}

    Counts of blanks removed : {}
    '''.format(clean_str, len(city) - len(clean_str)))

# example 3: create all possible permutations involving two sets and store
#            them in a new list
# --+ data
l_0 = [1, 2, 3]
l_1 = ['a', 'b', 'c']
# --+ container
output = []
# --+ nested for loop
for i in l_0:
    for j in l_1:
        to_append = [i, j]
        output.append(to_append)

output


# example 4: match the elements from two lists that occupy the same position
#            (i.e., have same index) and store them in a new list
# --+ container
output = []
# --+ now, the foor loop includes the generator 'zip' to create a 1-to-1
#     matching
for i, j in zip(l_0, l_1):
    to_append = [i, j]
    output.append(to_append)

output
