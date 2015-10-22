__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math


class MayanNumericalSystem:
    def __init__(self, base=20):
        self.base = base
        self.numbers = []
        for i in range(self.base):
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
            for j in range(self.base):
                self.numbers[j] += numeral[j*l:(j+1)*l]

    def get_number_graphical_representation(self, number : int):

        digits = []

        while number >= self.base:
            rest = number % self.base
            number = number // self.base
            digits.append(rest)
        digits.append(number)


        print("digits: " + str(digits), file=sys.stderr)

        r = ""
        for digit in reversed(digits):
            r += self.get_digit_graphical_representation(digit)

        return r

    def get_digit_graphical_representation(self, digit : int):
        r = ""
        for i in range(self.h):
            r += self.numbers[digit][i*self.l:(i+1)*self.l]
            r += "\n"
        return r

    def get_value(self, graphical_representation : str):
        for i, n in enumerate(self.numbers):
            if graphical_representation == n:
                return i

        return -1

    def get_number_from_input(self, number_of_lines_to_read : int):
        number = 0

        for i in range(number_of_lines_to_read // self.h - 1, -1, -1):
            r = ""
            for j in range(self.h):
                r += input()
            value = self.get_value(r)
            print("value: " + str(value), file=sys.stderr)
            number += value * pow(self.base, i)

        return number


ns = MayanNumericalSystem()

for i in range(20):
    print(ns.get_number_graphical_representation(i), file=sys.stderr)

s1 = int(input())
n1 = ns.get_number_from_input(s1)

s2 = int(input())
n2 = ns.get_number_from_input(s2)

operation = input()

print("n1: " + str(n1), file=sys.stderr)
print("n2: " + str(n2), file=sys.stderr)
print("operator: " + str(operation), file=sys.stderr)

result = -1
if operation == "+":
    result = n1 + n2
elif operation == "-":
    result = n1 - n2
elif operation == "*":
    result = n1 * n2
elif operation == "/":
    result = n1 // n2

print("result: " + str(result), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(ns.get_number_graphical_representation(result)[:-1])
