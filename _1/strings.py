#/usr/env/bin python3
# -*- encoding utf-8 -*-

"""
-----------------------------------------------------------------------------
    strings.py  |  Python objects
-----------------------------------------------------------------------------

Auhor  : simone.santoni.1@city.ac.uk

Agenda :

    + strings
      - let's make some order (and avoid stupid errors!)
      - string manipulation
      - single quotes, double quotes, and escape sequences
      - popular string methods

"""

# %% let's make some order
'''
let's make some order: Python is not a human being; what you interpret as a number could be a string for Python. All what is included among quotes - single or double - is a string. Let's consider the following:
'''
# a string
S0 = 'abc'
# another string
S1 = '123'
# test the type of S0 and S1
type(S0) == type(S1)

# %% string manipulation

# index to query a string's elements
# --+ let's retrieve the first element
S0[0]
# --+ and the last one
S0[-1]
# --+ the first two elements (note: the upper bound of the index, '2' in this
#     case is not retrieved)
S0[0:2]
# --+ slice the string to get the last two elements
S0[-2:]
# is it possible 'to sum' – i.e., to concatenate – strings?
# --+ yup
S0 + S1
# --+ use the join method to make your code more elegant and readable
''.join([S0, S1])
# --+ now play with the join method to use custom seprators
' -- '.join([S0, S1])
'******'.join([S0, S1])

# how about formatting scalar objects as strings?
# --+ option 1: use the builtin 'str' function
str(10)
# --+ option 2: use string formatting
# ----+ option 2a: compact version
'%s' % 10
# ----+ option 2b: 'format' builtin function
'{}'.format(10)
# --+ example
PRICE = 99.99
UNIT = '$'
'Price: {} {}'.format(UNIT, PRICE)

# %% single quotes, double quotes, and escape sequences

# strings are delimited by single or double quotes
# --+ single quotes – FINE!
S = 'Diplo is one of my favorite electronic music producers'
# --+ double quotes - FINE!
S = "Diplo is one of my favorite electronic music producers"
# --+ don't mix and match
S = "Diplo is one of my favorite electronic music producers'

# single and double quotes can be purposefully combined into the same string
# --+ example, the single quote is associated with the Saxon Genitive
#     in this case, the escape sequence '\' makes the single quote an
#     element of the string
S = "Diplo\'s latest single is hot"

# the escape sequence can also be used to pass non standard strings
# --+ e.g.: linefeed
print('\n'.join(['Hello', 'world!']))
# --+ e.g.: horizontal tab
print('\t'.join(['Hello', 'world!']))

# %% popular string methods
Method
center(width)
endswith(suffix) startswith(prefix) index(substring) lstrip([chars])
rstrip([chars]) strip([chars])
upper() lower() title()
replace(old, new) split([sep])
join([list]) isalpha()
isdigit() Description

# 'center' returns the string centered in a string with total number of characters width
S.center(50)
# 'endswith' returns True if the string ends with the substring suffix
S.endswith('hot')
# 'startswith' returns True if the string starts with the substring prefix.
S.startswith('Diplo')
# 'index' returns the lowest index in the string containing substring
S.index('hot')
# 'lstrip' ('rstrip') returns a copy of the string with any of the leading
#    (trailing) characters specified by [chars] removed. If [chars] is
#    omitted, any leading whitespace is removed
S.lstrip('Diplo')
# 'strip' returns a copy of the string with leading and trailing characters
#    specified by [chars] removed. If [chars] is omitted, any leading and #
#    trailing whitespace is removed.
' hello world! '.strip()
# 'upper' returns a copy of the string with all characters in uppercase
'hello world!'.upper()
# 'lower' returns a copy of the string with all characters in lowercase.
'HELLO WORLD!'.lower()
# 'title' returns a copy of the string with all words starting with capitals
#    and other characters in lowercase.
'hello world!'.title()
# 'replace' returns a copy of the string with each substring old replaced
#    with new
S.replace('Diplo', 'ESTA.')
# 'split' returns a list of substrings from the original string which are
#    separated by the string sep.If sep is not specified, the separator is
#    taken to be any amount of whitespace
'hellow world!'.split(' ')
# 'join' is the inverse of 'split'
' '.join(['hello', 'world!'])
# 'isalpha' returns True if all characters in the string are alphabetic and
#    the string is not empty; otherwise return False.
'hello'.isalpha()
# 'isdigit' returns True if all characters in the string are digits and the
#    string is not empty; otherwise return False.
'123'.isalpha()
'123'.isdigit()
