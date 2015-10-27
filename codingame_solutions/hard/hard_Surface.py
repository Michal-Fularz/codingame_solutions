__author__ = 'Amin'

import sys
import math


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.graphical_representation = []
        self.visited = []

        self.__init_from_input()

    def __init_from_input(self):
        for i in range(self.height):
            row = []
            row_visited = []
            for c in input():
                row.append(c)
                row_visited.append(False)

            self.graphical_representation.append(row)
            self.visited.append(row_visited)

    def __get_element(self, x, y):
        return self.graphical_representation[y][x]

    def __set_as_visited(self, x, y):
        self.visited[y][x] = True

    def __is_visited(self, x, y):
        return self.visited[y][x]

    def check_element(self, x, y):
        lake_size = 0

        if 0 <= x < self.width and 0 <= y < self.height:
            if self.__get_element(x, y) == "O" and not self.__is_visited(x, y):
                lake_size += 1
                # set this cell as visited
                self.__set_as_visited(x, y)
                # check elements around
                lake_size += self.check_element(x, y-1)
                lake_size += self.check_element(x-1, y)
                lake_size += self.check_element(x, y)
                lake_size += self.check_element(x+1, y)
                lake_size += self.check_element(x, y+1)

        return lake_size


    def clear_visited(self):
        for i in range(self.height):
            for j in range(self.width):
                self.visited[i][j] = False

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
                if cell:
                    r += "1"
                else:
                    r += "0"
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
    print("Lake size: " + str(lake_size), file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(lake_size)
