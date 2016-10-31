#!/usr/bin/env python

"""alternating-characters.py: Solution of the Question found at Algorithms>Strings>Alternating Characters"""

__author__      = "Risabh Kumar"


for _ in range(int(input())):
    count=0
    X=input()
    for i in range(len(X)-1):
        if X[i]==X[i+1]:
            count+=1
    print(count)



"""
# USING LIST COMPREHENSIONS IT CAN BE REDUCED TO

for X in [input() for _ in range(int(input()))]:
    print(len([i for i in range(len(X)-1) if X[i]==X[i+1]]))

"""