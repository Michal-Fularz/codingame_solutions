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

n = int(raw_input())
for i in xrange(n):
    x, y = [int(j) for j in raw_input().split()]
    homes.append((x, y))

max_x = max(homes, key=lambda tup: tup[0])
min_x = min(homes, key=lambda tup: tup[0])
max_y = max(homes, key=lambda tup: tup[1])
min_y = min(homes, key=lambda tup: tup[1])

print >> sys.stderr, "Max x: " + str(max_x)
print >> sys.stderr, "Min x: " + str(min_x)
print >> sys.stderr, "Max y: " + str(max_y)
print >> sys.stderr, "Min y: " + str(min_y)
print >> sys.stderr, "Sum y: " + str(sum(abs(y) for x, y in homes))

sorted_by_y = sorted(homes, key=lambda tup: tup[1])
print >> sys.stderr, "Sorted y: " + str(sorted_by_y)

median = 0
if n % 2 == 1:
    median = sorted_by_y[n/2]
else:
    median = ((sorted_by_y[n/2][0] + sorted_by_y[(n+1)/2][0])/2, (sorted_by_y[n/2][1] + sorted_by_y[(n+1)/2][1])/2)

print >> sys.stderr, "Median: " + str(median)

median_y = median[1]
distance = 0
for x, y in sorted_by_y:
    distance += abs(y - median_y)

distance += abs(max_x[0] - min_x[0])

print >> sys.stderr, "Distance: " + str(distance)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print distance