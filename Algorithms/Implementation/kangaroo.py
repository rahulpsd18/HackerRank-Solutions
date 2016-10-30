#!/usr/bin/env python

"""kangaroo.py: Solution of the Question found at Algorithms>Implementation>Kangaroo"""

__author__      = "Risabh Kumar"

import sys
import time

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
result=False
if v1<v1:
    result=False
else:    
    t_end = time.time() + 6
    while time.time() < t_end:
        x1+=v1
        x2+=v2
        if x1==x2:
            result=True
            break
print("YES" if result else "NO")