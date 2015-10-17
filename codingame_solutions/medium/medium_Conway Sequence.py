__author__ = 'Amin'

import sys
import math


def get_count_of_first_number(elements):
    count = 1
    number_to_look_for = elements[0]

    for number in elements[1:]:
        if number_to_look_for == number:
            count += 1
        else:
            break

    return number_to_look_for, count


r = int(input())
l = int(input())

current_line = [r]
new_line = []

for i in range(l-1):
    k = 0
    new_line = []
    print("Current line: " + str(current_line), file=sys.stderr)
    while k < len(current_line):
        number, count = get_count_of_first_number(current_line[k:])
        print("Processed fragment: " + str(current_line[k:]), file=sys.stderr)
        print("Number: " + str(number) + ", count: " + str(count), file=sys.stderr)
        new_line.append(count)
        new_line.append(number)
        k += count
    current_line = new_line

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

result = ""
for value in current_line:
    result += str(value) + " "

print(result[:-1])
