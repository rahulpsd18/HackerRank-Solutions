#!/usr/bin/env python

"""library-fine.py: Solution of the Question found at Algorithms>Implementation>Library Fine"""

__author__      = "Risabh Kumar"


d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

if (d2>=d1 and m2>=m1 and y2>=y1) or (m2>m1 and y2>=y1) or (y2>y1):
    fine=0
elif d2<d1 and m2==m1 and y2>=y1:
    fine=15*abs(d2-d1)
elif m2<m1 and y2==y1:
    fine=500*abs(m2-m1)
else:
    fine=10000
print(fine)