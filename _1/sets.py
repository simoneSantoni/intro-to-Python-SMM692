#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    sets.py  |  Python objects
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + sets
      - what's a set?
      - initializing a new set
      - sets: use cases
      -

"""

# %% what's a set?

"""
A set is an unordered collection of unique items. As with dictionary keys, elements of aset must be hashable objects. Aset isuseful forremoving duplicates fromasequence and for determining the union, intersection and difference between two collections. Because they are unordered, set objects cannot be indexed or sliced, but they can be iterated over, tested for membership, and they support the len built-in (Hill, 2015)
"""

# %% initializing a set

# option 1: listing elements between braces
s = ({'a', 'b', 'c'})
type(s)

# option 2: passing an iterable to set()
s = set(['a', 'b', 'c'])
type(s)

# %% sets: use cases

"""
'set' objects have a wide range of methods corresponding to the properties of
mathematical sets; see below
"""

""" CARDINALITY

- The cardinality of a set, |A|, is the number of elements it contains. Two
   sets are equal if they both contain the same elements.
"""
# the cardinality of l is 6
l = [0, 1, 9, 3, 3, 6, 6, 5]
len(set(l))

""" SUBSET/SUPERSET
- Set A is a subset of set B (A ⊆ B) if all the elements of A are also
   elements of B; set B is said to be a superset of set A.
"""
A, B = set([0, 1, 2]), set([0, 1])
A.issubset(B)
A.issuperset(B)
B.issubset(A)

""" PROPER SUBSET/SUPERSET
- Set A is a proper subset of B (A ⊂ B) if it is a subset of B but not equal
   to B; in this case, set B is said to be a proper superset of A.
"""
A > B
B < A

""" UNION
- The union of two sets (A ∪ B)is the set of all elements from both of them.
"""
A | B

""" INTERSECTION
- The intersection of two sets (A ∩ B) is the set of all elements they have
   in common.
"""
A & B
# or
A.intersection(B)

"""
- The difference of set A and set B (A\B) is the set of elements in A that
   are not in B.
"""
A.difference(B)

""" SYMMETRIC DIFFERENCE
- The symmetric difference of two sets, A△B, is the set of elements
   in either but not in both.
"""
set([0, 1]).symmetric_difference(set([1, 2]))

""" DISJOINT SETS
- Two sets are said to be disjoint if they have no elements in common.
"""
set([0, 1]).isdisjoint(set([2, 3]))
