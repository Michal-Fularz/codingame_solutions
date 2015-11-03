__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math
import numpy as np


class Building:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Width: " + str(self.width) + ", height: " + str(self.height), file=sys.stderr)

        self.map = np.zeros((self.height, self.width), dtype="int8")
        print(self.map, file=sys.stderr)

    def __mark_up_right_as_empty(self, current_x, current_y):
        self.map[0:current_y+1, current_x:self.width] = 1
        # for y in range(0, current_y+1):
        #     for x in range(current_x, self.width):
        #         self.map[y, x] = 1

    def __mark_up_left_as_empty(self, current_x, current_y):
        self.map[0:current_y+1, 0:current_x+1] = 1
        # for y in range(0, current_y+1):
        #     for x in range(0, current_x+1):
        #         self.map[y, x] = 1

    def __mark_down_right_as_empty(self, current_x, current_y):
        self.map[current_y:self.height, current_x:self.width] = 1
        # for y in range(current_y, self.height):
        #     for x in range(current_x, self.width):
        #         self.map[y, x] = 1

    def __mark_down_left_as_empty(self, current_x, current_y):
        self.map[current_y:self.height, 0:current_x+1] = 1
        # for y in range(current_y, self.height):
        #     for x in range(0, current_x+1):
        #         self.map[y, x] = 1

    def mark_part_as_empty(self, current_x, current_y, bomb_direction):
        if bomb_direction == "U":
            self.__mark_down_left_as_empty(current_x, current_y)
            self.__mark_down_right_as_empty(current_x, current_y)

        elif bomb_direction == "UR":
            self.__mark_up_left_as_empty(current_x, current_y)
            self.__mark_down_left_as_empty(current_x, current_y)
            self.__mark_down_right_as_empty(current_x, current_y)

        elif bomb_direction == "R":
            self.__mark_up_left_as_empty(current_x, current_y)
            self.__mark_down_left_as_empty(current_x, current_y)

        elif bomb_direction == "DR":
            self.__mark_up_left_as_empty(current_x, current_y)
            self.__mark_up_right_as_empty(current_x, current_y)
            self.__mark_down_left_as_empty(current_x, current_y)

        elif bomb_direction == "D":
            self.__mark_up_left_as_empty(current_x, current_y)
            self.__mark_up_right_as_empty(current_x, current_y)

        elif bomb_direction == "DL":
            self.__mark_up_left_as_empty(current_x, current_y)
            self.__mark_up_right_as_empty(current_x, current_y)
            self.__mark_down_right_as_empty(current_x, current_y)

        elif bomb_direction == "L":
            self.__mark_up_right_as_empty(current_x, current_y)
            self.__mark_down_right_as_empty(current_x, current_y)

        elif bomb_direction == "UL":
            self.__mark_up_right_as_empty(current_x, current_y)
            self.__mark_down_left_as_empty(current_x, current_y)
            self.__mark_down_right_as_empty(current_x, current_y)

        print(self.map, file=sys.stderr)

    def find_movements(self, bomb_direction):
        vertical_movement = 0
        horizontal_movement = 0

        if bomb_direction == "U":
            vertical_movement = 1
        elif bomb_direction == "UR":
            vertical_movement = 1
            horizontal_movement = 1
        elif bomb_direction == "R":
            horizontal_movement = 1
        elif bomb_direction == "DR":
            vertical_movement = -1
            horizontal_movement = 1
        elif bomb_direction == "D":
            vertical_movement = -1
        elif bomb_direction == "DL":
            vertical_movement = -1
            horizontal_movement = -1
        elif bomb_direction == "L":
            horizontal_movement = -1
        elif bomb_direction == "UL":
            vertical_movement = 1
            horizontal_movement = -1

        return vertical_movement, horizontal_movement

    def find_distance_available(self, current_x, current_y, vertical_movement, horizontal_movement):

        distance_available_vertical = 0
        x = current_x
        y = current_y
        if vertical_movement == 1:
            # UP
            while y >= 0 and self.map[y][x] == 0:
                distance_available_vertical += 1
                y -= 1
        elif vertical_movement == -1:
            # DOWN
            while y < self.height and self.map[y][x] == 0:
                distance_available_vertical += 1
                y += 1

        distance_available_horizontal = 0
        x = current_x
        y = current_y
        if horizontal_movement == -1:
            # LEFT
            while x >= 0 and self.map[y][x] == 0:
                distance_available_horizontal += 1
                x -= 1
        elif horizontal_movement == 1:
            # RIGHT
            while x < self.width and self.map[y][x] == 0:
                distance_available_horizontal += 1
                x += 1

        return distance_available_vertical, distance_available_horizontal


# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

building = Building(w, h)

current_x = x0
current_y = y0

# game loop
while 1:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # choose direction
    vertical_movement, horizontal_movement = building.find_movements(bomb_dir)

    distance_available_vertical, distance_available_horizontal = \
        building.find_distance_available(current_x, current_y, vertical_movement, horizontal_movement)

    # calculate the distance to travel
    building.mark_part_as_empty(current_x, current_y, bomb_dir)

    current_x += horizontal_movement * (distance_available_horizontal // 2)
    current_y -= vertical_movement * (distance_available_vertical // 2)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # the location of the next window Batman should jump to.
    print(str(current_x) + " " + str(current_y))
