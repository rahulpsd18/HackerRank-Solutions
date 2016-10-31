#!/usr/bin/env python

"""sherlock-and-squares.py: Solution of the Question found at Algorithms>Implementation>sherlock-and-squares"""

__author__      = "Risabh Kumar"

import math
T=int(input())
for t in range(T):
    counter=0
    test=input().split()
    lower,upper=[int(test[0]),int(test[1])]
    print(math.floor(math.sqrt(upper))-math.ceil(math.sqrt(lower))+1)