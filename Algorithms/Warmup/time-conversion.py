#!/usr/bin/env python

"""time-conversion.py: Solution of the Question found at Algorithms>Warmup>Time Conversion"""

__author__      = "Risabh Kumar"

from time import strptime, strftime
print(strftime("%H:%M:%S", strptime(input(), "%I:%M:%S%p")))