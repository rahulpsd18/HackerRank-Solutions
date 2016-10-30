#!/usr/bin/env python

"""a-very-big-sum.py: Solution of the Question found at Algorithms>Warmup>A Very Big Sum"""

__author__      = "Risabh Kumar"

n,num,sum=int(input()),input(),0
for i in range(n):
    sum+=int(num.split()[i])
print(sum)