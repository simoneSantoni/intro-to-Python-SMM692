#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    control_flow.py  |  Control flow, iterators/loops
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + the if statement
    + conditional foor loops ― examples

"""

# %% the if statement

"""
Few computer programs are executed in a purely linear fashion, one
statement after another as written in the source code. It is more likely that
during the program execution, data objects are inspected and blocks of code
executed conditionally on the basis of some test carried out on them. Thus,
all practical languages have the equivalent of an if-then-(else) construction.
(Hill, 2015).
"""

# typical conditional execution of a program
# --+ data
fruits = ['apple', 'orange', 'pineapple']
# --+ foor loop + if statement
for fruit in fruits:
    if fruit == 'apple':
        print('{} ― fruit or company?'.format(fruit))
    elif fruit == 'orange':
        print('{} contains C vitamin'.format(fruit))
    else:
        pass

# %% conditional for loops ― examples

# sample data
# --+ columns are company, sector, stock market
company_data = [['a', 'finacial services', 'UK'],
                ['b', 'automotive', 'DE']]
# --+ data are nested within companies; columns are company, year, return on
#   equity (%)
profitability = [['a', 2018, 5.2],
                 ['b', 2018, 4.3],
                 ['a', 2019, 5.8],
                 ['b', 2019, 4.6]]

# example 1: merge company data and profitability for the most recent year
merge = []
for i in company_data:
    for j in profitability:
        if i[0] == j[0]:               # match data with respect to comapnies
            to_append = i + j[1:]
            merge.append(to_append)
        else:
            pass                       # do nothing

merge

# example 2: merge company data and profitability for the most recent year
merge = []
for i in company_data:
    for j in profitability:
        if i[0] == j[0]:               # match data with respect to comapnies
            if j[1] == 2019:           # retain most recent data
                to_append = i + j[1:]
                merge.append(to_append)
            else:
                pass                   # do nothing
        else:
            pass

merge

# example 3: redo 2 by avoiding nested if statements
merge = []
for i in company_data:
    for j in profitability:
        if (i[0] == j[0]) & (j[1] == 2019): # match data on company and year
            to_append = i + j[1:]
            merge.append(to_append)
        else:
            pass

merge
