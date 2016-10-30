#!/usr/bin/env python

"""compare-the-triplets.py: Solution of the Question found at Algorithms>Warmup>Compare the Triplets"""

__author__      = "Risabh Kumar"

a = list(map(int,input().strip().split(' ')))
b = list(map(int,input().strip().split(' ')))
A,B = 0,0
for x,y in zip(a,b):
    if (x>y):
        A+=1
    elif (y>x):
        B+=1
print(A,B)