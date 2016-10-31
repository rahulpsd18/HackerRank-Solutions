#!/usr/bin/env python

"""repeated-string.py: Solution of the Question found at Algorithms>Implementation>Repeated String"""

__author__      = "Risabh Kumar"

s, n = input().strip(), int(input().strip())
l=(s.count('a')*(n//len(s))) #for the complete words
r=(s[:n%len(s)].count('a')) #for the incomplete words
print(l+r)