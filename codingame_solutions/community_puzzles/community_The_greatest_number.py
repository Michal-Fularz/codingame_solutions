import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
line = input().replace(" ", "")

values = list(line)
print(values, file=sys.stderr)

flag_dot = False
if "." in values:
    flag_dot = True
    values.remove(".")

flag_sign = False
if "-" in values:
    flag_sign = True
    values.remove("-")

flag_zeros = False
number_of_zeros = 0
if "0" in values:
    flag_zeros = True
    number_of_zeros = values.count("0")
    values = [value for value in values if value != "0"]

values = [int(x) for x in values]
values.sort()

print(values, file=sys.stderr)
print("zeros: " + str(flag_zeros) + ", count: " + str(number_of_zeros), file=sys.stderr)

answer = ""
if flag_sign:

    if len(values) > 0:
        answer += "-"

        if flag_dot:
            if flag_zeros:
                answer += "0"
                number_of_zeros -= 1
            else:
                answer += str(values.pop(0))
            answer += "."
        else:
            answer += str(values.pop(0))

        if flag_zeros:
            for i in range(0, number_of_zeros):
                answer += "0"

        for value in values:
            answer += str(value)
    else:
        answer += "0"

else:
    if len(values) > 1:
        for value in reversed(values[1:]):
            answer += str(value)

        if flag_dot:
            answer += "."

        answer += str(values[0])

    elif len(values) == 1:
        answer += str(values[0])

    else:
        answer += "0"

    if flag_zeros:
        for i in range(0, number_of_zeros-1):
            answer += "0"

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#print("greatest")
print(answer)

