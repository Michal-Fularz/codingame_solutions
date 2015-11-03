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

        self.map = np.zeros((self.height, self.width))#, dtype=np.uint8)
        print(self.map, file=sys.stderr)

        self.odd_movement = False

    def update_map(self, batman, bomb_distance):

        if bomb_distance == "SAME":
            if batman.direction_current == Direction.down:
                distance_traveled = batman.y_current - batman.y_previous

                y_start = batman.y_previous + distance_traveled // 2
                y_end = batman.y_current - distance_traveled // 2 + 1

                self.map[0:y_start, :] = -1
                self.map[y_end:self.height, :] = -1

            elif batman.direction_current == Direction.up:
                distance_traveled = batman.y_previous - batman.y_current

                y_start = batman.y_current + distance_traveled // 2
                y_end = batman.y_previous - distance_traveled // 2 + 1

                self.map[0:y_start, :] = -1
                self.map[y_end:self.height, :] = -1

            # this part is done only when the right row is chosen
            elif batman.direction_current == Direction.left:
                distance_traveled = batman.x_previous - batman.x_current

                x_start = batman.x_current + distance_traveled // 2
                x_end = batman.x_previous - distance_traveled // 2 + 1

                self.map[batman.y_current, 0:x_start] = -1
                self.map[batman.y_current, x_end:self.width] = -1

                #print(self.map[batman.y_current], file=sys.stderr)

            elif batman.direction_current == Direction.right:
                distance_traveled = batman.x_current - batman.x_previous

                x_start = batman.x_previous + distance_traveled // 2
                x_end = batman.x_current - distance_traveled // 2 + 1

                self.map[batman.y_current, 0:x_start] = -1
                self.map[batman.y_current, x_end:self.width] = -1

                #print(self.map[batman.y_current], file=sys.stderr)

            else:
                pass

        elif bomb_dist == "WARMER":
            if batman.direction_current == Direction.down:
                distance_traveled = batman.y_current - batman.y_previous

                y_start = batman.y_previous + distance_traveled // 2 + 1

                self.map[0:y_start, :] = -1

            elif batman.direction_current == Direction.up:
                distance_traveled = batman.y_previous - batman.y_current

                y_end = batman.y_previous - distance_traveled // 2

                self.map[y_end:self.height, :] = -1

            # this part is done only when the right row is chosen
            elif batman.direction_current == Direction.left:
                distance_traveled = batman.x_previous - batman.x_current

                x_end = batman.x_previous - distance_traveled // 2

                self.map[batman.y_current, x_end:self.width] = -1

                #print(self.map[batman.y_current], file=sys.stderr)

            elif batman.direction_current == Direction.right:
                distance_traveled = batman.x_current - batman.x_previous

                x_start = batman.x_previous + distance_traveled // 2 + 1

                self.map[batman.y_current, 0:x_start] = -1

                #print(self.map[batman.y_current], file=sys.stderr)

        elif bomb_distance == "COLDER":
            if batman.direction_current == Direction.down:
                distance_traveled = batman.y_current - batman.y_previous

                y_end = batman.y_current - distance_traveled // 2

                self.map[y_end:self.height, :] = -1

            elif batman.direction_current == Direction.up:
                distance_traveled = batman.y_previous - batman.y_current

                y_start = batman.y_current + distance_traveled // 2 + 1

                self.map[0:y_start, :] = -1


            # this part is done only when the right row is chosen
            elif batman.direction_current == Direction.left:
                distance_traveled = batman.x_previous - batman.x_current

                x_start = batman.x_current + distance_traveled // 2 + 1

                self.map[batman.y_current, 0:x_start] = -1
                #print(self.map[batman.y_current], file=sys.stderr)

            elif batman.direction_current == Direction.right:
                distance_traveled = batman.x_current - batman.x_previous

                x_end = batman.x_current - distance_traveled // 2

                self.map[batman.y_current, x_end:self.width] = -1
                #print(self.map[batman.y_current], file=sys.stderr)

        #print(self.map, file=sys.stderr)

    def __update_map_distance_closer(self, x_start, x_end, y_start, y_end, flag_closer, flag_further):
        # iterate over all the cells, calculate previous and current distance and mark those that are closer / further than in previous step
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

                    if flag_closer and not flag_further:
                        print("Remove those that are closer", file=sys.stderr)
                        if distance_current < distance_previous:
                            self.map[y][x] = distance_current

                    if flag_further and not flag_closer:
                        print("Remove those that are further", file=sys.stderr)
                        if distance_current > distance_previous:
                            self.map[y][x] = distance_current

                    if flag_further and flag_closer:
                        print("ERROR!!!", file=sys.stderr)
                    if not flag_further and not flag_closer:
                        print("ERROR!!!", file=sys.stderr)

    def find_movements_based_on_distance(self, bat, bomb_distance):

        direction = batman.direction_current

        free_cells_in_current_direction = self.__count_number_of_free_cells_in_that_direction(bat.x_current, bat.y_current, direction)
        free_cells_in_opposing_direction = self.__count_number_of_free_cells_in_that_direction(bat.x_current, bat.y_current, Direction.get_opposite(direction))

        print("Free cells in current direction: " + str(free_cells_in_current_direction), file=sys.stderr)
        print("Free cells in opposing direction: " + str(free_cells_in_opposing_direction), file=sys.stderr)

        if bomb_distance == "WARMER":
            # last time we moved in right direction
            direction = bat.direction_current

            if free_cells_in_opposing_direction > free_cells_in_current_direction:
                direction = Direction.get_opposite(bat.direction_current)
                print("Change direction in work!", file=sys.stderr)

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

    def __count_number_of_free_cells_in_that_direction(self, current_x, current_y, direction ):
        free_cells = 0
        if direction == Direction.up:
            # check column above
            print("Checking column above", file=sys.stderr)
            for y in range(0, current_y):
                if self.map[y][current_x] == 0:
                    free_cells += 1
        elif direction == Direction.down:
            # check column below
            print("Checking column below", file=sys.stderr)
            for y in range(current_y+1, self.height):
                if self.map[y][current_x] == 0:
                    free_cells += 1
        if direction == Direction.left:
            # check row on the left
            print("Checking row on the left", file=sys.stderr)
            for x in range(0, current_x):
                if self.map[current_y][x] == 0:
                    free_cells += 1
        elif direction == Direction.right:
            # check column below
            print("Checking row on the right", file=sys.stderr)
            for x in range(current_x+1, self.width):
                if self.map[current_y][x] == 0:
                    free_cells += 1
        return free_cells

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
            new_position = self.height//2# - current_y
        else:
            direction = Direction.up
            new_position = self.height//2# - current_y

        return direction, new_position

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
        elif direction == Direction.right:
            for x in range(current_x+1, self.width):
                if self.map[current_y][x] == 0:
                    available_points.append(x)
        elif direction == Direction.left:
            for x in range(0, current_x):
                if self.map[current_y][x] == 0:
                    available_points.append(x)


        #available_points.sort()
        next_position = sum(available_points) / len(available_points)

        #if next_position - int(next_position) > 0:
            #next_position += 1

        if not self.odd_movement:
            if direction == Direction.up:
                pass
                #next_position = available_points[int(0.25*len(available_points))]
                #next_position = min(available_points)
            elif direction == Direction.down:
                #pass
                #next_position = available_points[int(0.75*len(available_points))]
                next_position = max(available_points)
            elif direction == Direction.left:
                #pass
                #next_position = available_points[int(0.25*len(available_points))]
                next_position = min(available_points)
            elif direction == Direction.right:
                pass
                #next_position = available_points[int(0.75*len(available_points))]
                #next_position = max(available_points)
            #self.odd_movement = True

        # if self.odd_movement:
        #     if direction == Direction.up:
        #         next_position = available_points[int(0.25*len(available_points))]
        #     elif direction == Direction.down:
        #         next_position = available_points[int(0.75*len(available_points))]
        #     elif direction == Direction.left:
        #         next_position = available_points[int(0.25*len(available_points))]
        #     elif direction == Direction.right:
        #         next_position = available_points[int(0.75*len(available_points))]
        #     self.odd_movement = False

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
current_direction, new_pos = building.find_movements_first_round(batman.x_current, batman.y_current)

batman.update_based_on_direction2(current_direction, new_pos)
batman.direction_previous = current_direction

print(str(batman.x_current) + " " + str(batman.y_current))

# game loop
while 1:
    previous_bomb_dist = bomb_dist
    bomb_dist = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)

    building.update_map(batman, bomb_dist)

    current_direction = building.find_movements_based_on_distance(batman, bomb_dist)
    print("Direction choosen: " + str(current_direction), file=sys.stderr)
    new_pos = building.find_next_position(batman.x_current, batman.y_current, current_direction)
    print("Distance available: " + str(new_pos), file=sys.stderr)
    batman.update_based_on_direction2(current_direction, new_pos)
    print(batman.get_as_string(), file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(str(batman.x_current) + " " + str(batman.y_current))
