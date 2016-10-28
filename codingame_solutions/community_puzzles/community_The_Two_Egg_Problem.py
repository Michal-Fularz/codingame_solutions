import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

flag_continue = True
n_remaining = n
step = 1
while n_remaining > step:
    n_remaining = n_remaining - step
    step = step + 1

print("n_remaining: " + str(n_remaining) + ", step: " + str(step), file=sys.stderr)

n_current = 0
for i in range(step, 0, -1):
    n_current = n_current + i
    print("n_current:" + str(n_current) + ", operations to do: " + str(i-1), file=sys.stderr)




# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(step)
#print("42")
