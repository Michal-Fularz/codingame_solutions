__author__ = 'Amin'

import sys
import math


n = int(raw_input())
horses = []
for i in xrange(n):
    horses.append(int(raw_input()))

horses.sort()

minimal_difference = 9999999

for i in xrange(len(horses)-1):
    difference = abs(horses[i] - horses[i+1])
    if difference < minimal_difference:
        minimal_difference = difference

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print minimal_difference
