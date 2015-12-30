__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math

n = int(input())
vs = input()

stock_values = []

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
# To debug: print("Debug messages...", file=sys.stderr)

print(stock_values, file=sys.stderr)

print(global_difference)
