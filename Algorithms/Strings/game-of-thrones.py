#!/usr/bin/env python

"""game-of-thrones.py: Solution of the Question found at Algorithms>Strings>Game of Thrones - I"""

__author__      = "Risabh Kumar"

s = input()
if len([c for c in set(s) if s.count(c) % 2 != 0]) < 2:
    print('YES')
else:
    print('NO')