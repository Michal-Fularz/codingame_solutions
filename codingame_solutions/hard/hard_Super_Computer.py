__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math

calculations = []

n = int(input())
for i in range(n):
    starting_day, duration = [int(j) for j in input().split()]
    calculations.append((starting_day, duration))

calculations.sort(key=lambda tup: tup[0])
print(calculations, file=sys.stderr)

number_of_executed_calculations = 0

calculations_to_be_executed = []
planned_starting_day = 0
planned_end_day = 0
for calculation in calculations:
    current_starting_day = calculation[0]
    current_end_day = current_starting_day + calculation[1]

    if current_starting_day >= planned_end_day:
        number_of_executed_calculations += 1
        calculations_to_be_executed.append((planned_starting_day, planned_end_day))
        planned_starting_day = current_starting_day
        planned_end_day = current_end_day
    elif current_end_day <= planned_end_day:
        planned_starting_day = current_starting_day
        planned_end_day = current_end_day

# add last planned calculations to the list and remove first one (it is just 0, 0)
calculations_to_be_executed.append((planned_starting_day, planned_end_day))
calculations_to_be_executed = calculations_to_be_executed[1:]
# it is not needed to increase number_of_executed_calculations because one additional (0, 0) calculation is already in

print(calculations_to_be_executed, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(number_of_executed_calculations)
