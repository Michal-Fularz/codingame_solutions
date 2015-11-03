__author__ = 'Amin'

import sys
import math
import numpy as np
from enum import Enum


class Direction(Enum):
    up = 1
    down = 2
    left = 3
    right = 4

    @staticmethod
    def get_opposite(direction):
        if direction == Direction.up:
            return Direction.down
        elif direction == Direction.down:
            return Direction.up
        elif direction == Direction.right:
            return Direction.left
        elif direction == Direction.left:
            return Direction.right


class Building:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Width: " + str(self.width) + ", height: " + str(self.height), file=sys.stderr)

        self.map = np.zeros((self.height, self.width))#, dtype="int8")
        print(self.map, file=sys.stderr)

    def __mark_up_right_as_empty(self, current_x, current_y):
        self.map[0:current_y+1, current_x:self.width] = 1

    def __mark_up_left_as_empty(self, current_x, current_y):
        self.map[0:current_y+1, 0:current_x+1] = 1

    def __mark_down_right_as_empty(self, current_x, current_y):
        self.map[current_y:self.height, current_x:self.width] = 1

    def __mark_down_left_as_empty(self, current_x, current_y):
        self.map[current_y:self.height, 0:current_x+1] = 1

    def update_map(self, batman, bomb_distance, flag_first_round):

        #print("Current: " + str(batman.x_current) + ", " + str(batman.y_current), file=sys.stderr)
        #print("Previous: " + str(batman.x_previous) + ", " + str(batman.y_previous), file=sys.stderr)

        if bomb_distance == "SAME":
            if batman.direction_current == Direction.down:
                distance_traveled = batman.y_current - batman.y_previous

                y_start = batman.y_previous + distance_traveled // 2
                y_end = batman.y_current - distance_traveled // 2
                if y_end >= self.height:
                    y_end = self.height

                self.map[0:y_start, :] = -1
                self.map[y_end:self.height, :] = -1

                #self.__update_map_distance_further(0, self.width, y_start, y_end)

            elif batman.direction_current == Direction.up:
                distance_traveled = batman.y_previous - batman.y_current

                y_start = batman.y_current - distance_traveled // 2 + 1
                if y_start < 0:
                    y_start = 0
                y_end = batman.y_previous - distance_traveled // 2 + 1

                self.map[0:y_start, :] = -1
                self.map[y_end:self.height, :] = -1

                #self.__update_map_distance_further(0, self.width, y_start, y_end)

            # this part is done only when the right row is chosen
            elif batman.direction_current == Direction.left:
                distance_traveled = batman.x_previous - batman.x_current

                x_start = batman.x_current + distance_traveled // 2 - 1
                x_end = batman.x_previous - distance_traveled // 2 + 1

                self.map[batman.y_current, 0:x_start] = -1
                self.map[batman.y_current, x_end:self.width] = -1

            elif batman.direction_current == Direction.right:
                distance_traveled = batman.x_current - batman.x_previous

                x_start = batman.x_previous + distance_traveled // 2 - 1
                x_end = batman.x_current - distance_traveled // 2 + 1

                self.map[batman.y_current, 0:x_start] = -1
                self.map[batman.y_current, x_end:self.width] = -1

            else:
                pass

        elif bomb_dist == "WARMER":
            if flag_first_round:
                if batman.direction_current == Direction.down:
                    self.map[0:batman.y_current, :] = -1
                elif batman.direction_current == Direction.up:
                    self.map[batman.y_current:self.height, :] = -1
            else:
                if batman.direction_current == Direction.down:
                    distance_traveled = batman.y_current - batman.y_previous

                    y_start = batman.y_previous + distance_traveled // 2 + 1

                    # remove all the rows that were above previous position
                    self.map[0:y_start, :] = -1

                    #self.__update_map_distance_further(0, self.width, y_start, y_end)
                elif batman.direction_current == Direction.up:
                    distance_traveled = batman.y_previous - batman.y_current

                    y_start = batman.y_current - distance_traveled
                    if y_start < 0:
                        y_start = 0
                    y_end = batman.y_previous - distance_traveled // 2

                    # remove all the rows that were below previous position
                    self.map[y_end:self.height, :] = -1
                    # remove all the rows that are above
                    self.map[0:y_start, :] = -1

                    #self.__update_map_distance_further(0, self.width, y_start, y_end)

                # this part is done only when the right row is chosen
                elif batman.direction_current == Direction.left:
                    distance_traveled = batman.x_previous - batman.x_current

                    x_start = 0
                    x_end = batman.x_previous - distance_traveled // 2
                    if x_end >= self.width:
                        x_end = self.width - 1

                    self.map[batman.y_current, x_end:self.width] = -1

                elif batman.direction_current == Direction.right:
                    distance_traveled = batman.x_current - batman.x_previous

                    x_start = batman.x_previous + distance_traveled // 2
                    if x_start < 0:
                        x_start = 0
                    x_end = self.width - 1

                    self.map[batman.y_current, 0:x_start] = -1

                else:
                    self.__update_map_distance_further(0, self.width, 0, self.height)

        elif bomb_distance == "COLDER":
            if flag_first_round:
                if batman.direction_current == Direction.down:
                    self.map[batman.y_current:self.height, :] = -1
                elif batman.direction_current == Direction.up:
                    self.map[0:batman.y_current, :] = -1
            else:
                if batman.direction_current == Direction.down:
                    distance_traveled = batman.y_current - batman.y_previous

                    y_end = batman.y_previous + distance_traveled // 2 + 1
                    if y_end >= self.height:
                        y_end = self.height

                    # remove all the rows that were below previous position
                    self.map[y_end:self.height, :] = -1

                    #self.__update_map_distance_further(0, self.width, y_start, y_end)
                elif batman.direction_current == Direction.up:
                    distance_traveled = batman.y_previous - batman.y_current

                    y_start = batman.y_previous - distance_traveled // 2
                    if y_start < 0:
                        y_start = 0

                    # remove all the rows that were above previous position
                    self.map[0:y_start, :] = -1

                    #self.__update_map_distance_further(0, self.width, y_start, y_end)


                # this part is done only when the right row is chosen
                elif batman.direction_current == Direction.left:
                    distance_traveled = batman.x_previous - batman.x_current

                    x_start = batman.x_current + distance_traveled // 2

                    self.map[batman.y_current, 0:x_start] = -1

                elif batman.direction_current == Direction.right:
                    distance_traveled = batman.x_current - batman.x_previous

                    x_end = batman.y_current - distance_traveled // 2

                    self.map[batman.y_current, x_end:self.width] = -1

                else:
                    self.__update_map_distance_further(0, self.width, 0, self.height)

        print(self.map, file=sys.stderr)

    def __update_map_distance_closer(self, x_start, x_end, y_start, y_end):
        # iterate over all the cells, calculate previous and current distance and mark those that are closer than in previous step
        print("Remove those that are closer", file=sys.stderr)
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                if self.map[y][x] == 0:
                    # TODO: POSSIBLE IMPROVEMENTS:
                    # initial:
                    # distance_previous = math.sqrt(pow(batman.x_previous - x, 2) + pow(batman.y_previous - y, 2))
                    # distance_current = math.sqrt(pow(batman.x_current - x, 2) + pow(batman.y_current - y, 2))
                    # remove sqrt!
                    # distance_previous = pow(batman.x_previous - x, 2) + pow(batman.y_previous - y, 2)
                    # distance_current = pow(batman.x_current - x, 2) + pow(batman.y_current - y, 2)
                    # change pow to multiply
                    distance_previous = (batman.x_previous - x) * (batman.x_previous - x) + (batman.y_previous - y) * (batman.y_previous - y)
                    distance_current = (batman.x_current - x) * (batman.x_current - x) + (batman.y_current - y) * (batman.y_current - y)

                    if distance_current < distance_previous:
                        self.map[y][x] = distance_current

    def __update_map_distance_further(self, x_start, x_end, y_start, y_end):
        # iterate over all the cells, calculate previous and current distance and mark those that are further than in previous step
        print("Remove those that are further", file=sys.stderr)
        print("x_start: " + str(x_start) + ", x_end: " + str(x_end), file=sys.stderr)
        print("y_start: " + str(y_start) + ", y_end: " + str(y_end), file=sys.stderr)
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                if self.map[y][x] == 0:
                    # TODO: POSSIBLE IMPROVEMENTS:
                    # initial:
                    # distance_previous = math.sqrt(pow(batman.x_previous - x, 2) + pow(batman.y_previous - y, 2))
                    # distance_current = math.sqrt(pow(batman.x_current - x, 2) + pow(batman.y_current - y, 2))
                    # remove sqrt!
                    # distance_previous = pow(batman.x_previous - x, 2) + pow(batman.y_previous - y, 2)
                    # distance_current = pow(batman.x_current - x, 2) + pow(batman.y_current - y, 2)
                    # change pow to multiply
                    distance_previous = (batman.x_previous - x) * (batman.x_previous - x) + (batman.y_previous - y) * (batman.y_previous - y)
                    distance_current = (batman.x_current - x) * (batman.x_current - x) + (batman.y_current - y) * (batman.y_current - y)

                    if distance_current > distance_previous:
                        self.map[y][x] = distance_current

    def find_movements_based_on_distance(self, bat, bomb_distance):

        direction = batman.direction_current

        if bomb_distance == "WARMER":
            # last time we moved in right direction
            direction = bat.direction_current
        elif bomb_distance == "COLDER":
            direction = Direction.get_opposite(bat.direction_current)
        elif bomb_distance == "SAME":
            pass

        print("First direction guess: " + str(direction), file=sys.stderr)

        # check if move is possible
        if not self.__check_if_there_are_free_cells_in_that_direction(bat.x_current, batman.y_current, direction):
            if self.__check_if_there_are_free_cells_in_that_direction(bat.x_current, batman.y_current, Direction.up):
                return Direction.up
            if self.__check_if_there_are_free_cells_in_that_direction(bat.x_current, batman.y_current, Direction.down):
                return Direction.down
            if self.__check_if_there_are_free_cells_in_that_direction(bat.x_current, batman.y_current, Direction.right):
                return Direction.right
            if self.__check_if_there_are_free_cells_in_that_direction(bat.x_current, batman.y_current, Direction.left):
                return Direction.left

        return direction

    def __check_if_there_are_free_cells_in_that_direction(self, current_x, current_y, direction):
        if direction == Direction.up:
            # check column above
            print("Checking column above", file=sys.stderr)
            for y in range(0, current_y):
                if self.map[y][current_x] == 0:
                    return True
        elif direction == Direction.down:
            # check column below
            print("Checking column below", file=sys.stderr)
            for y in range(current_y+1, self.height):
                if self.map[y][current_x] == 0:
                    return True
        if direction == Direction.left:
            # check row on the left
            print("Checking row on the left", file=sys.stderr)
            for x in range(0, current_x):
                if self.map[current_y][x] == 0:
                    return True
        elif direction == Direction.right:
            # check column below
            print("Checking row on the right", file=sys.stderr)
            for x in range(current_x+1, self.width):
                if self.map[current_y][x] == 0:
                    return True
        return False

    # bomb_distance = UNKNOWN
    def find_movements_first_round(self, current_x, current_y):

        if current_y < (self.height // 2):
            direction = Direction.down
        else:
            direction = Direction.up

        return direction

    def find_next_position(self, current_x, current_y, direction):

        available_points = []

        if direction == Direction.up:
            for y in range(0, current_y):
                if self.map[y][current_x] == 0:
                    available_points.append(y)
        elif direction == Direction.down:
            for y in range(current_y+1, self.height):
                if self.map[y][current_x] == 0:
                    available_points.append(y)
        elif direction == Direction.left:
            for x in range(0, current_x):
                if self.map[current_y][x] == 0:
                    available_points.append(x)
        elif direction == Direction.right:
            for x in range(current_x+1, self.width):
                if self.map[current_y][x] == 0:
                    available_points.append(x)

        next_position = sum(available_points) / len(available_points)

        return int(next_position)


class Batman:
    def __init__(self, x0, y0):
        self.x_initial = x0
        self.y_initial = y0

        self.x_current = self.x_initial
        self.y_current = self.y_initial

        self.x_previous = self.x_initial
        self.y_previous = self.y_initial

        self.direction_current = Direction.up
        self.direction_previous = Direction.up

    def update(self, dx, dy):
        self.x_previous = self.x_current
        self.y_previous = self.y_current

        self.x_current += dx
        self.y_current -= dy

    def update_based_on_direction(self, direction, distance):
        self.x_previous = self.x_current
        self.y_previous = self.y_current

        self.direction_previous = self.direction_current
        self.direction_current = direction

        if direction == Direction.up:
            self.y_current -= distance
        elif direction == Direction.down:
            self.y_current -= -distance
        elif direction == Direction.right:
            self.x_current += distance
        elif direction == Direction.left:
            self.x_current += -distance

    def update_based_on_direction2(self, direction, new_pos):
        self.x_previous = self.x_current
        self.y_previous = self.y_current

        self.direction_previous = self.direction_current
        self.direction_current = direction

        if direction == Direction.up:
            self.y_current = new_pos
        elif direction == Direction.down:
            self.y_current = new_pos
        elif direction == Direction.right:
            self.x_current = new_pos
        elif direction == Direction.left:
            self.x_current = new_pos

    def get_new_position_based_on_direction(self, direction, distance):
        new_x = self.x_current
        new_y = self.y_current

        if direction == Direction.up:
            new_y -= distance
        elif direction == Direction.down:
            new_y -= -distance
        elif direction == Direction.right:
            new_x += distance
        elif direction == Direction.left:
            new_x += -distance

        return new_x, new_y

    def get_as_string(self):
        r = "Batman position: \n"
        r += "x: " + str(self.x_current) + ", y: " + str(self.y_current) + "\n"
        r += "x_p: " + str(self.x_previous) + ", y_p: " + str(self.y_previous) + "\n"
        r += "dir: " + str(self.direction_current) + ", dir_p: " + str(self.direction_previous)

        return r


# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

building = Building(w, h)
batman = Batman(x0, y0)

# IDEAS:
# use abs to calculate distance instead of power and square root - maybe it will be faster
# THOSE TWO METRICS GIVES DIFFERENT VALUES
# b = np.zeros((5, 5))
# for i in range(5):
#     for j in range(5):
#         b[i][j] = math.sqrt(pow(i-3, 2)+pow(j-4, 2))
# print(b)
#
# a = np.zeros((5, 5))
# for i in range(5):
#     for j in range(5):
#         a[i][j] = abs(i-3) + abs(j-4)
# print(a)

flag_first_round = True

bomb_dist = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)

# first round is special - bomb_distance = UNKNOWN
#vertical_movement, horizontal_movement = building.find_movements_first_round(batman.x_current, batman.y_current)
current_direction = building.find_movements_first_round(batman.x_current, batman.y_current)

#batman.update(horizontal_movement, vertical_movement)
batman.update_based_on_direction(current_direction, 1)
batman.direction_previous = current_direction

print(str(batman.x_current) + " " + str(batman.y_current))

# game loop
while 1:
    previous_bomb_dist = bomb_dist
    bomb_dist = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)

    building.update_map(batman, bomb_dist, flag_first_round)
    if flag_first_round:
        flag_first_round = False

    #vertical_movement, horizontal_movement = building.find_movements_based_on_distance(batman, bomb_dist)
    current_direction = building.find_movements_based_on_distance(batman, bomb_dist)
    print("Direction choosen: " + str(current_direction), file=sys.stderr)
    #current_distance_available = building.find_distance_available(batman.x_current, batman.y_current, current_direction)
    new_pos = building.find_next_position(batman.x_current, batman.y_current, current_direction)
    print("Distance available: " + str(new_pos), file=sys.stderr)

    #batman.update(horizontal_movement, vertical_movement)
    batman.update_based_on_direction2(current_direction, new_pos)

    print(batman.get_as_string(), file=sys.stderr)


    # # choose direction
    # vertical_movement, horizontal_movement = building.find_movements(bomb_dir)
    #
    # distance_available_vertical, distance_available_horizontal = \
    #     building.find_distance_available(current_x, current_y, vertical_movement, horizontal_movement)
    #
    # # calculate the distance to travel
    # building.mark_part_as_empty(current_x, current_y, bomb_dir)
    #
    # current_x += horizontal_movement * (distance_available_horizontal // 2)
    # current_y -= vertical_movement * (distance_available_vertical // 2)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(str(batman.x_current) + " " + str(batman.y_current))
