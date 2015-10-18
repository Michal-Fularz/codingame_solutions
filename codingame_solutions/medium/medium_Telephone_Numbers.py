__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math


class ContactManagerElement:
    def __init__(self, number=-1):
        self.digit = number
        self.next = []

    def contains(self, digit: int):
        for element in self.next:
            if element.digit == digit:
                return True
        return False

    def add_digit(self, digit: int):
        if not self.contains(digit):
            new_element = ContactManagerElement(digit)
            self.next.append(new_element)
            return new_element
        else:
            return next(x for x in self.next if x.digit == digit)

    def add(self, telephone_number: list):
        current_element = self

        for digit in telephone_number:
            current_element = current_element.add_digit(digit)

    def count_elements(self):
        # do not take into account first element (root)
        if self.digit == -1:
            count = 0
        else:
            count = 1

        for element in self.next:
            count += element.count_elements()

        return count


n = int(input())

contact_manager = ContactManagerElement()
for i in range(n):
    telephone_number = [int(digit) for digit in input()]
    print(telephone_number, file=sys.stderr)
    contact_manager.add(telephone_number)

number_of_elements = contact_manager.count_elements()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# The number of elements (referencing a number) stored in the structure.
print(number_of_elements)
