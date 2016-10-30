#!/usr/bin/env python

"""angry-professor.py: Solution of the Question found at Algorithms>Implementation>Angry Professor"""

__author__      = "Risabh Kumar"

t=int(input())
for _ in range(t):
    c=0
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]<=0:
            c+=1
    print("YES" if c<k else "NO")