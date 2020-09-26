#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    dictionaries.py  |  Python objects
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + dictionaries
      - definition – what's a dictionary?
      - initializing a dictionary
      - querying dictionary's data
      - changing a dictionary's value(s)
      - nested dictionaries

"""

# %% what's a dictionary?

'''
A dictionary in Python is a type of “associative array” (also known as a
“hash” in some languages). A dictionary can contain any objects as its
values,but unlike sequences such as lists and tuples, in which the items are
indexed by an integer starting at 0, each item in a dictionary is indexed by a
unique key,which maybeany immutable object.4 The dictionary therefore exists
as a number of key-value pairs, which do not have any particular order.
Dictionaries themselves are mutable objects (Hill, 2015 – Learning scientific
Programming with Python)
'''

# %% initializing a dictionary

# option 1: including pairs of keys and values within braces
d = {'customer_0': 'xxxx@gmail.com', 'customer_1': 'yyyy@city.ac.uk'}

# option 2: passing lists to the dict function
data = ['customer_0', 'xxxx@gmail.com'], ['customer_1', 'yyyy@city.ac.uk']
d = dict(data)
d
# or, more elegant:
ids = ['customer_0', 'customer_1']
emails = ['xxxx:gmail.com', 'yyyy@city.ac.uk']
d = dict(zip(ids, emails))
d

# %% querying dictionary's data

# WARNING: you can't index dictionaries by position – use keys instead!
#    For example, let's get the email of the customer with 'customer_0'
d['customer_0']

# the keys of a dictionary can be returned by calling the 'keys' method
keys = d.keys()

# ...whereas values can be returned with the 'values' method
values = d.values()

# starting from the set of keys, it's easy to iterate over the dictionary
for key in keys:
    print('Customer email: {}'.format(d[key]))

# %% changing a dictionary's value(s)

# I don't like playing with the contents of the dictionaries;
#     if you really want to change the values of a dictionary don't forget
#     to use keys as indices
d['customer_0'] = 'unknown_email_address'
d
# --+ this doesn't produce the expected resul
d[0] = 'my_email'
d

# there's also a dictionary method to update extant values
d1 = {'customer_0': 'the_new_email@me.com'}
d.update(d1)
d

# %% dictionaries nested in dictionaries

# NOTE: dictionaries can contain nested data
# --+ initializing a nested dictionary
d = {'company_0': {'location': 'UK',
                   'profit': {'year_0': 4, 'year_1_profit': 10},
                   'sector': 'financial_services'},
     'company_1': {'location': 'FR',
                   'profit': {'year_0': 2, 'year_1_profit': 11},
                   'sector': 'insurance'}}
# --+ clean print of the dictionary
from pprint import pprint as pp
pp(d)
# --+ let's inspect the keys of d – 'location', 'profit', 'sector' are
#     the three keys nested within the higher level key, that is, the set
#     of companies
for key in d.keys():
    print(key, d[key].keys())
