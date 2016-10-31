#!/usr/bin/env python

"""super-reduced-string.py: Solution of the Question found at Algorithms>Strings>Super Reduced String"""

__author__      = "Risabh Kumar"

import re #importing re to make use of regex

inp=input().strip()
regex=re.compile(r'(\D)(\1)',re.M|re.I)
search=regex.search(inp)
while search:
    inp=inp.replace(search.group(),'')
    search=regex.search(inp)
print(inp if inp else 'Empty String')