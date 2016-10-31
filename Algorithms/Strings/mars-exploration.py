#!/usr/bin/env python

"""mars-exploration.py: Solution of the Question found at Algorithms>Strings>Mars Exploration"""

__author__      = "Risabh Kumar"

count,i,j=0,0,0
tmp=('S','O','S')
S = input().strip()
for i in range(len(S)):
    if j==3:
        j=0
    if S[i] != tmp[j]:
        count+=1
    j+=1
print(count)