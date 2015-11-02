__author__ = 'Amin'

import sys
import math
import numpy as np


class Building:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.map = np.zeros((self.height, self.width))
        print(self.map, file=sys.stderr)

    def __mark_quarter_up_right_as_empty(self, current_x, current_y):
        for y in range(0, current_y):
            for x in range(current_x, self.width):
                self.map[y][x] = 1

    def __mark_quarter_up_left_as_empty(self, current_x, current_y):
        for y in range(0, current_y):
            for x in range(0, current_x):
                self.map[y][x] = 1

    def __mark_quarter_down_right_as_empty(self, current_x, current_y):
        for y in range(current_y, self.height):
            for x in range(current_x, self.width):
                self.map[y][x] = 1

    def __mark_quarter_down_left_as_empty(self, current_x, current_y):
        for y in range(current_y, self.height):
            for x in range(0, current_x):
                self.map[y][x] = 1

    def mark_part_as_empty(self, current_x, current_y, direction):
        if bomb_dir == "U":
            self.__mark_quarter_down_left_as_empty(current_x, current_y)
            self.__mark_quarter_down_right_as_empty(current_x, current_y)

        elif bomb_dir == "UR":
            self.__mark_quarter_up_left_as_empty(current_x, current_y)
            self.__mark_quarter_down_left_as_empty(current_x, current_y)
            self.__mark_quarter_down_right_as_empty(current_x, current_y)

        elif bomb_dir == "R":
            self.__mark_quarter_up_left_as_empty(current_x, current_y)
            self.__mark_quarter_down_left_as_empty(current_x, current_y)

        elif bomb_dir == "DR":
            self.__mark_quarter_up_left_as_empty(current_x, current_y)
            self.__mark_quarter_up_right_as_empty(current_x, current_y)
            self.__mark_quarter_down_left_as_empty(current_x, current_y)

        elif bomb_dir == "D":
            self.__mark_quarter_up_left_as_empty(current_x, current_y)
            self.__mark_quarter_up_right_as_empty(current_x, current_y)

        elif bomb_dir == "DL":
            self.__mark_quarter_up_left_as_empty(current_x, current_y)
            self.__mark_quarter_up_right_as_empty(current_x, current_y)
            self.__mark_quarter_down_right_as_empty(current_x, current_y)

        elif bomb_dir == "L":
            self.__mark_quarter_up_right_as_empty(current_x, current_y)
            self.__mark_quarter_down_right_as_empty(current_x, current_y)

        elif bomb_dir == "UL":
            self.__mark_quarter_up_right_as_empty(current_x, current_y)
            self.__mark_quarter_down_left_as_empty(current_x, current_y)
            self.__mark_quarter_down_right_as_empty(current_x, current_y)

        print(self.map, file=sys.stderr)


# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

building = Building(w, h)

current_x = x0
current_y = y0

previous_x = x0
previous_y = y0

# game loop
while 1:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    vertical_movement = 0
    horizontal_movement = 0

    # choose direction
    if bomb_dir == "U":
        vertical_movement = 1
    elif bomb_dir == "UR":
        vertical_movement = 1
        horizontal_movement = 1
    elif bomb_dir == "R":
        horizontal_movement = 1
    elif bomb_dir == "DR":
        vertical_movement = -1
        horizontal_movement = 1
    elif bomb_dir == "D":
        vertical_movement = -1
    elif bomb_dir == "DL":
        vertical_movement = -1
        horizontal_movement = -1
    elif bomb_dir == "L":
        horizontal_movement = -1
    elif bomb_dir == "UL":
        vertical_movement = 1
        horizontal_movement = -1

    # calculate the distance to travel
    building.mark_part_as_empty(current_x, current_y, bomb_dir)


    previous_x = current_x
    previous_y = current_y

    current_x += horizontal_movement
    current_y -= vertical_movement

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # the location of the next window Batman should jump to.
    print(str(current_x) + " " + str(current_y))
