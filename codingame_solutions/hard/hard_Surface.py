__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math
import numpy as np


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.graphical_representation = []
        self.visited = np.zeros((self.height, self.width))

        self.__init_from_input()

    def __init_from_input(self):
        for i in range(self.height):
            row = []
            for c in input():
                row.append(c)

            self.graphical_representation.append(row)

    def __get_element(self, x, y):
        return self.graphical_representation[y][x]

    def __set_as_visited(self, x, y):
        self.visited[y][x] = 1

    def __is_visited(self, x, y):
        if self.visited[y][x] == 1:
            return True
        else:
            return False

    def check_element_recursive(self, x, y):
        lake_size = 0

        if 0 <= x < self.width and 0 <= y < self.height:
            if self.__get_element(x, y) == "O" and not self.__is_visited(x, y):
                lake_size += 1
                # set this cell as visited
                self.__set_as_visited(x, y)
                # check elements around
                lake_size += self.check_element(x, y-1)
                lake_size += self.check_element(x-1, y)
                lake_size += self.check_element(x+1, y)
                lake_size += self.check_element(x, y+1)

        return lake_size

    def check_element(self, x, y):
        lake_size = 0

        elements_to_check = [(x, y)]

        while len(elements_to_check) > 0:
            element_to_check = elements_to_check.pop(0)
            x_to_check = element_to_check[0]
            y_to_check = element_to_check[1]
            # check first element from the list
            if 0 <= x_to_check < self.width and 0 <= y_to_check < self.height:
                if self.__get_element(x_to_check, y_to_check) == "O" and not self.__is_visited(x_to_check, y_to_check):
                    lake_size += 1
                    # set this cell as visited
                    self.__set_as_visited(x_to_check, y_to_check)
                    # add elements around to be checked
                    elements_to_check.append((x_to_check, y_to_check-1))
                    elements_to_check.append((x_to_check-1, y_to_check))
                    elements_to_check.append((x_to_check+1, y_to_check))
                    elements_to_check.append((x_to_check, y_to_check+1))

        return lake_size

    def clear_visited(self):
        self.visited = np.zeros((self.height, self.width))

    def set_visited(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == j:
                    self.visited[i][j] = True

    def get_graphical_representation_as_string(self):
        r = ""

        for row in self.graphical_representation:
            for c in row:
                r += c
            r += "\n"

        return r

    def get_visited_as_string(self):
        r = ""

        for row in self.visited:
            for cell in row:
                r += str(cell)
            r += "\n"

        return r


l = int(input())
h = int(input())

m = Map(l, h)
print("Map: \n" + m.get_graphical_representation_as_string(), file=sys.stderr)
print("Map: \n" + m.get_visited_as_string(), file=sys.stderr)

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    lake_size = m.check_element(x, y)
    m.clear_visited()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(lake_size)
