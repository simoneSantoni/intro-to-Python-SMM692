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
# --+ we need an iterable object
l = ['Apple', 'Microsoft', 'Lenovo', 'Intel']
# --+ let's print out the names of these companies one by one
