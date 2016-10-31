#!/usr/bin/env python

"""utopian-tree.py: Solution of the Question found at Algorithms>Implementation>Utopian Tree"""

__author__      = "Risabh Kumar"

T=int(input())
for t in range(T):
    x=int(input())
    height=1;
    if x==0:
        print(height)
    else:
        while x!=0:
            height=height*2
            x-=1
            if x==0:
                break
            else:
                height+=1
                x-=1
        print(height)