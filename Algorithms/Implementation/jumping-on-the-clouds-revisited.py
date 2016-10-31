#!/usr/bin/env python

"""jumping-on-the-clouds-revisited.py: Solution of the Question found at Algorithms>Implementation>Jumping on the Clouds: Revisited"""

__author__      = "Risabh Kumar"

n,k = map(int,input().strip().split(' '))
c = [int(c_temp) for c_temp in input().strip().split(' ')]
print(100-sum(1+2*c[i] for i in range(0,n,k)))