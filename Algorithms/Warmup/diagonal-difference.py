#!/usr/bin/env python

"""diagonal-difference.py: Solution of the Question found at Algorithms>Warmup>Diagonal Difference"""

__author__      = "Risabh Kumar"

n=int(input())
sum1,sum2=0,0
r1,r2=0,n-1
for i in range(n):
    str_inp=input().split()
    sum1+=int(str_inp[r1])
    sum2+=int(str_inp[r2])
    r1=r1+1
    r2=r2-1
print(abs(sum1-sum2))