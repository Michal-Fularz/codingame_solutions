__author__ = 'Amin'

import sys
import math


n = int(raw_input()) # the number of temperatures to analyse
temps = list((int(temp) for temp in raw_input().split())) # the n temperatures expressed as integers ranging from -273 to 5526

closest_temp = 9999
closest_difference = abs(closest_temp)
for temp in temps:
    difference = abs(temp)
    if difference < closest_difference or (difference == closest_difference and temp > closest_temp):
        closest_temp = temp
        closest_difference = difference

for item in temps:
    print >> sys.stderr, str(item) + ", "

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

if len(temps) == 0:
    print 0
else:
    print closest_temp
