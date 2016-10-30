#!/usr/bin/env python

"""sock-merchant.py: Solution of the Question found at Algorithms>Implementation>Sock Merchant"""

__author__      = "Risabh Kumar"

import sys

count=0
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
for i in set(c):
    tmp=c.count(i)
    if tmp>=2:
        count+=(tmp//2)
print(count)