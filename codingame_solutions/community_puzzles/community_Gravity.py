import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width, height = [int(i) for i in input().split()]
lines = []
for i in range(height):
    line = list(input())
    lines.append(line)

print("\n".join(map(str, lines)), file=sys.stderr)

flag_change = True
while flag_change:
    flag_change = False
    for row in range(height-2, -1, -1):
        for col in range(0, width):
            if lines[row][col] == "#" and lines[row+1][col] == ".":
                lines[row][col] = "."
                lines[row + 1][col] = "#"
                flag_change = True

print("\n".join(map(str, lines)), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("\n".join(["".join(line) for line in lines]))
