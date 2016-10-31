#!/usr/bin/env python

"""jumping-on-the-clouds.py: Solution of the Question found at Algorithms>Implementation>Jumping on the Clouds"""

__author__      = "Risabh Kumar"

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i=0
count=0
c=c+[0]
while i!=(n-1):
    if(c[i+2]==0 and i<(n-2)):
        i+=2
        count+=1
    else:
        i+=1
        count+=1
print(count)