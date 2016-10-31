#!/usr/bin/env python

"""strange-counter.py: Solution of the Question found at Algorithms>Implementation>Strange Counter"""

__author__      = "Risabh Kumar"

t = int(input().strip())
rem = 3
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)