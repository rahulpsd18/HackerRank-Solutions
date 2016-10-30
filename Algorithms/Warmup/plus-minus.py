#!/usr/bin/env python

"""plus-minus.py: Solution of the Question found at Algorithms>Warmup>Plus Minus"""

__author__      = "Risabh Kumar"

size=int(input())
neg=pos=zer=0
inp_str=input().split()
for i in range(size):
    if int(inp_str[i])>0:
        pos+=1
    elif int(inp_str[i])<0:
        neg+=1
    else:
        zer+=1
print(pos/size,neg/size,zer/size,sep='\n')