__author__ = 'Amin'

import sys
import math

# Weber problem
# http://www.matstos.pjwstk.edu.pl/no10/no10_mlodak.pdf
# https://en.wikipedia.org/wiki/Weber_problem
# https://en.wikipedia.org/wiki/Geometric_median

# simple solution:
# find the median point and that is all!

homes = []

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    homes.append((x, y))

max_x = max(homes, key=lambda tup: tup[0])
min_x = min(homes, key=lambda tup: tup[0])
max_y = max(homes, key=lambda tup: tup[1])
min_y = min(homes, key=lambda tup: tup[1])

print("Max x: " + str(max_x), file=sys.stderr)
print("Min x: " + str(min_x), file=sys.stderr)
print("Max y: " + str(max_y), file=sys.stderr)
print("Min y: " + str(min_y), file=sys.stderr)
print("Sum y: " + str(sum(abs(y) for x, y in homes)), file=sys.stderr)

sorted_by_y = sorted(homes, key=lambda tup: tup[1])
print("Sorted y: " + str(sorted_by_y), file=sys.stderr)

median = 0
if n % 2 == 1:
    median = sorted_by_y[n//2]
else:
    median = ((sorted_by_y[n//2][0] + sorted_by_y[(n+1)//2][0])/2, (sorted_by_y[n//2][1] + sorted_by_y[(n+1)//2][1])/2)

print("Median: " + str(median), file=sys.stderr)

median_y = median[1]
distance = 0
for x, y in sorted_by_y:
    distance += abs(y - median_y)

distance += abs(max_x[0] - min_x[0])

print("Distance: " + str(distance), file=sys.stderr)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print(int(distance))
