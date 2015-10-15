__author__ = 'Amin'

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
vs = raw_input()

stock_values = []#[5, 3, 4, 2, 3, 1]

for value in vs.split(" "):
    stock_values.append(int(value))

start_value = stock_values[0]
difference = 0
global_difference = 0
trend = 0

for stock_value in stock_values:
    if trend == 0:
        if stock_value < start_value:
            # downward trend
            trend = -1
            difference = stock_value - start_value
        else:
            # nothing changes, update starting value
            start_value = stock_value
    elif trend == -1:
        if stock_value < start_value:
            current_difference = (stock_value - start_value)
            if current_difference < difference:
                difference = current_difference
        elif stock_value > start_value:
            trend = 0
            start_value = stock_value
            if difference < global_difference:
                global_difference = difference

# additional check in case all values were in downward trend
if difference < global_difference:
    global_difference = difference

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print >> sys.stderr, stock_values

print global_difference
