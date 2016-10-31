#!/usr/bin/env python

"""funny-string.py: Solution of the Question found at Algorithms>Strings>Funny String"""

__author__      = "Risabh Kumar"


for w in [input() for _ in range(int(input()))]:
    wr=w[::-1]
    print("Funny" if all((abs(ord(wr[i])-ord(wr[i-1]))==abs(ord(w[i])-ord(w[i-1]))) for i in range(1,len(w))) else "Not Funny")
