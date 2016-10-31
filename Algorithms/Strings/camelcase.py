#!/usr/bin/env python

"""camelcase.py: Solution of the Question found at Algorithms>Strings>CamelCase"""

__author__      = "Risabh Kumar"


import re #importing re to make use of regex

s = input().strip()
print(len(re.findall(r'[A-Z]',s))+1)






""""
# ANOTHER WAY TO DO THIS


count=0
s = input().strip()
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        count+=1
print(count+1)

"""
