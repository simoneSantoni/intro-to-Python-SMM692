#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    lists.py  |  Python objects
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + lists:
      - initializing a new list
      - changing a list
      - indexing and slicing
      - methods for list manipulation

"""

# %% initializing a new list

# a list with int
l = [0, 1, 2, 3]

# lists are flexible – you can have multiple types of objects
l = ['a', 0, 0.995, 'hi there']

# %% changing a list (yup, lists are mutable)

# let's change the first element
l[0] = 'b'
l

# let's change the fourth element so as to have a list within a list
l[3] = ['hi', 'there']
l

# %% indexing and slicing

# the elements of a list are indexed by position
l[0]


# %% methods for list manipulation

# adding a new element in the target position
l = ['old_1', 'old_2']
l.insert(2, 'new')
l

# removing the first occurrence of an element from an existing element
l.remove('old_1')
l

# appending a new element to the end of the list
l.append('appended')
l

# 'extend' expands on an existing list
l.extend(['extend_1', 'extend_2'])
l

# sorting the list in place
l = [3, 2, 1]
l.sort()
l

# reversing the elements of a list
l.reverse()
l

# counting the instances of an element in the list
l = [0, 0, 99, 1000]
l.count(0)

# copying an existing list
copied = l.copy()
copied
