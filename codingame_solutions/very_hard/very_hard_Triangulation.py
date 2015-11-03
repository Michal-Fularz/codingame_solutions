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

        self.map = np.zeros((self.height, self.width), dtype="int8")
        print(self.map, file=sys.stderr)

    def __mark_up_right_as_empty(self, current_x, current_y):
        self.map[0:current_y+1, current_x:self.width] = 1

    def __mark_up_left_as_empty(self, current_x, current_y):
        self.map[0:current_y+1, 0:current_x+1] = 1

    def __mark_down_right_as_empty(self, current_x, current_y):
        self.map[current_y:self.height, current_x:self.width] = 1

    def __mark_down_left_as_empty(self, current_x, current_y):
        self.map[current_y:self.height, 0:current_x+1] = 1

    def update_map(self, batman, bomb_distance):

        #print("Current: " + str(batman.x_current) + ", " + str(batman.y_current), file=sys.stderr)
        #print("Previous: " + str(batman.x_previous) + ", " + str(batman.y_previous), file=sys.stderr)

        if bomb_distance == "SAME":
            pass
        elif bomb_distance == "WARMER":
            # iterate over all the cells, calculate previous and current distance and mark those that are further than in previous step
            print("Remove those that are further", file=sys.stderr)
            for i in range(self.height):
                for j in range(self.width):
                    distance_previous = math.sqrt(pow(batman.x_previous - j, 2) + pow(batman.y_previous - i, 2))
                    distance_current = math.sqrt(pow(batman.x_current - j, 2) + pow(batman.y_current - i, 2))

                    if distance_current > distance_previous:
                        self.map[i][j] = distance_current

        elif bomb_distance == "COLDER":
            # iterate over all the cells, calculate previous and current distance and mark those that are further than in previous step
            print("Remove those that are closer", file=sys.stderr)
            for i in range(self.height):
                for j in range(self.width):
                    distance_previous = math.sqrt(pow(batman.x_previous - j, 2) + pow(batman.y_previous - i, 2))
                    distance_current = math.sqrt(pow(batman.x_current - j, 2) + pow(batman.y_current - i, 2))

                    if distance_current < distance_previous:
                        self.map[i][j] = 100+distance_current

        print(self.map, file=sys.stderr)

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
        # new_x, new_y = bat.get_new_position_based_on_direction(current_direction, 1)
        # if self.map[new_y][new_x] != 0:
        #     # check available directions
        #     new_x, new_y = bat.get_new_position_based_on_direction(Direction.up)
        #     if self.map[new_y][new_x] == 0:
        #         return Direction.up
        #     new_x, new_y = bat.get_new_position_based_on_direction(Direction.down)
        #     if self.map[new_y][new_x] == 0:
        #         return Direction.down
        #     new_x, new_y = bat.get_new_position_based_on_direction(Direction.left)
        #     if self.map[new_y][new_x] == 0:
        #         return Direction.left
        #     new_x, new_y = bat.get_new_position_based_on_direction(Direction.right)
        #     if self.map[new_y][new_x] == 0:
        #         return Direction.right

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

    building.update_map(batman, bomb_dist)

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
