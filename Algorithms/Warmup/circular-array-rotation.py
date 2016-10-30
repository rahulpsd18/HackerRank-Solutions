#!/usr/bin/env python

"""circular-array-rotation.py: Solution of the Question found at Algorithms>Warmup>Circular Array Rotation"""

__author__      = "Risabh Kumar"

n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
k=k%n
arr=arr[-k:]+arr[:-k]
for i in range(q):
    X=int(input())
    print(arr[X])