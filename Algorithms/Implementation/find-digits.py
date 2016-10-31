#!/usr/bin/env python

"""find-digits.py: Solution of the Question found at Algorithms>Implementation>Find Digits"""

__author__      = "Risabh Kumar"

T=int(input())
for t in range(T):
    x=int(input())
    a=[]
    temp=x
    counter=0
    length=(len(str(x)))
    for l in range(length):
        a.append(temp%10)
        temp=int(temp/10)
    for l in range(length):
        if a[l]!=0:
            if x%a[l]==0:
                counter+=1
    print(counter)