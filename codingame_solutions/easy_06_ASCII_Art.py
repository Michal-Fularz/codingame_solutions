__author__ = 'Amin'

import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(raw_input())
H = int(raw_input())
T = raw_input()
T = T.upper()
print >> sys.stderr, "text: " + T
for i in xrange(H):
    ROW = raw_input()

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    output_line = ""

    for letter in T:
        if ord("A") <= ord(letter) <= ord("Z"):
            index_of_letter = ord(letter) - ord("A")
        else:
            index_of_letter = len(ROW) / L - 1
        print >> sys.stderr, "index_of_letter: " + str(index_of_letter)
        for j in xrange(0, L):
            output_line += ROW[index_of_letter * L + j]


    print output_line