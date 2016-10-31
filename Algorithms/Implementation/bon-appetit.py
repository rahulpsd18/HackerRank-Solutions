#!/usr/bin/env python

"""bon-appetit.py: Solution of the Question found at Algorithms>Implementation>Bon Appétit"""

__author__      = "Risabh Kumar"

N,K=map(int,input().split())
arr=[int(i) for i in input().split()]
bc=int(input())
tmp,ba=0,0
for i in range(N):
    if i==K:
        continue
    tmp+=arr[i]
ba=(int(tmp/2))
if ba==bc:
    print("Bon Appetit")
else:
    print(bc-ba)