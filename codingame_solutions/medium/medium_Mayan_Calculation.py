__author__ = 'Amin'

import sys
import math


class MayanNumericalSystem:
    def __init__(self):
        self.numbers = []
        for i in range(20):
            self.numbers.append("")

        self.l = 0
        self.h = 0

        self.__read_from_input()

    def __read_from_input(self):
        l, h = [int(i) for i in input().split()]
        self.l = l
        self.h = h
        for i in range(h):
            numeral = input()
            for j in range(20):
                self.numbers[j] += numeral[j*l:(j+1)*l]

    def get_number_graphical_representation(self, number):
        r = ""
        for i in range(self.h):
            r += self.numbers[number][i*self.l:(i+1)*self.l]
            r += "\n"
        return r

    def get_value(self, graphical_representation):
        for i, n in enumerate(self.numbers):
            if graphical_representation == n:
                return i

        return -1


ns = MayanNumericalSystem()

for i in range(20):
    print(ns.get_number_graphical_representation(i), file=sys.stderr)

s1 = int(input())
n1 = ""
for i in range(s1):
    n1 += input()
s2 = int(input())
n2 = ""
for i in range(s2):
    n2 += input()
operation = input()

print("n1: " + str(n1), file=sys.stderr)
print("n1 value: " + str(ns.get_value(n1)), file=sys.stderr)

print("n2: " + str(n2), file=sys.stderr)
print("n2 value: " + str(ns.get_value(n2)), file=sys.stderr)



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("result")
