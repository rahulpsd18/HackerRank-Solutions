#!/usr/bin/env python

"""the-love-letter-mystery.py: Solution of the Question found at Algorithms>Strings>The Love-Letter Mystery"""

__author__      = "Risabh Kumar"


for _ in range(int(input())):
    count=0
    word=input()
    for i in range(len(word)//2):
        if word[i]!=word[-i-1]:
            count+=abs(ord(word[i])-ord(word[-i-1]))
    print(count)



"""   
# USING LIST COMPREHENSIONS IT CAN BE REDUCED TO

for word in [input() for _ in range(int(input()))]:
    print(sum([abs(ord(word[i])-ord(word[-i-1])) for i in range(len(word)//2) if word[i]!=word[-i-1]]))

"""