#!/usr/bin/env python

"""save-the-prisoner.py: Solution of the Question found at Algorithms>Implementation>Save the Prisoner!"""

__author__      = "Risabh Kumar"

T=int(input())
for _ in range(T):
    N,M,S=map(int,input().strip().split())
    S=(S+M)%N
    if(S==1):
        print(N)
    else:
        print(S-1)