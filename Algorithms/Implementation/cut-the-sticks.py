#!/usr/bin/env python

"""cut-the-sticks.py: Solution of the Question found at Algorithms>Implementation>Cut the sticks"""

__author__      = "Risabh Kumar"

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while len(arr)>=1:
    print(len(arr))
    minm=min(arr)    
    arr=[temp-minm for temp in arr if (temp-minm)>0]