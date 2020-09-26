#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    tuples.py  |  Python objects
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + lists:
      -

"""

# %% initializing a tuple

# the elemnts of a tuple are delimited with parentheses
t = ('a', 1, 5.64)


# %% changing a tuple?

# NOTE: In a nutshell, tuples are immutable lists
# --+ it's possible to index and slice tuples
t[0]
t[0:2]
# --+ while it's not possible to change the elements of a tuple
t[0] = 'b'
# --+ hower, it's possible to change the list within a tuple
t = (0, ['a', 'b'])
t[1][1] = 'z'
t
# NOTE: such a possibility is consistent with the rationale of tuple, that is, preserving the order of some elements
