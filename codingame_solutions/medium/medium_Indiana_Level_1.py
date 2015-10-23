__author__ = 'Amin'

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while 1:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print("0 0")
