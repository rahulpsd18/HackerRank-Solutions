#!/usr/bin/env python

"""staircase.py: Solution of the Question found at Algorithms>Warmup>Staircase"""

__author__      = "Risabh Kumar"

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "#"*i)