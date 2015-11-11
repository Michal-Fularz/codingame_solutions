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
    mixed = 5

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
        elif direction == Direction.mixed:
            return Direction.mixed
        else:
            print("ERROR!!! This direction does not have implementation of this function!", file=sys.stderr)


class Movements(Enum):
    vertical = 1
    horizontal = 2
    mixed = 3

    @staticmethod
    def get_opposite(movement):
        if movement == Movements.vertical:
            return Movements.horizontal
        elif movement == Movements.horizontal:
            return Movements.vertical
        else:
            return Movements.mixed


class Building:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.usable_x_min = 0
        self.usable_x_max = self.width

        self.usable_y_min = 0
        self.usable_y_max = self.height

        self.map = np.zeros((self.height, self.width))  #, dtype=np.uint8)

    def update_map(self, batman, bomb_distance):

        if bomb_distance == "SAME":
            if batman.direction_current == Direction.down:
                distance_traveled = batman.y_current - batman.y_previous

                y_start = batman.y_previous + distance_traveled // 2
                y_end = batman.y_current - distance_traveled // 2 + 1

                self.map[self.usable_y_min:y_start, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_min = y_start
                self.map[y_end:self.usable_y_max, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_max = y_end

            elif batman.direction_current == Direction.up:
                distance_traveled = batman.y_previous - batman.y_current

                y_start = batman.y_current + distance_traveled // 2
                y_end = batman.y_previous - distance_traveled // 2 + 1

                self.map[self.usable_y_min:y_start, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_min = y_start
                self.map[y_end:self.usable_y_max, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_max = y_end

            elif batman.direction_current == Direction.left:
                distance_traveled = batman.x_previous - batman.x_current

                x_start = batman.x_current + distance_traveled // 2
                x_end = batman.x_previous - distance_traveled // 2 + 1

                self.map[self.usable_y_min:self.usable_y_max, self.usable_x_min:x_start] = -1
                self.usable_x_min = x_start
                self.map[self.usable_y_min:self.usable_y_max, x_end:self.usable_x_max] = -1
                self.usable_x_max = x_end

            elif batman.direction_current == Direction.right:
                distance_traveled = batman.x_current - batman.x_previous

                x_start = batman.x_previous + distance_traveled // 2
                x_end = batman.x_current - distance_traveled // 2 + 1

                self.map[self.usable_y_min:self.usable_y_max, self.usable_x_min:x_start] = -1
                self.usable_x_min = x_start
                self.map[self.usable_y_min:self.usable_y_max, x_end:self.usable_x_max] = -1
                self.usable_x_max = x_end

            else:
                # TODO: this is special case and can be treated accordingly
                # if last direction is one of up_right, up_left, down_right, down_left do not update the map
                pass

        elif bomb_dist == "WARMER":
            if batman.direction_current == Direction.down:
                distance_traveled = batman.y_current - batman.y_previous

                y_start = batman.y_previous + distance_traveled // 2 + 1

                self.map[self.usable_y_min:y_start, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_min = y_start

            elif batman.direction_current == Direction.up:
                distance_traveled = batman.y_previous - batman.y_current

                y_end = batman.y_previous - distance_traveled // 2

                self.map[y_end:self.usable_y_max, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_max = y_end

            elif batman.direction_current == Direction.left:
                distance_traveled = batman.x_previous - batman.x_current

                x_end = batman.x_previous - distance_traveled // 2

                self.map[self.usable_y_min:self.usable_y_max, x_end:self.usable_x_max] = -1
                self.usable_x_max = x_end

            elif batman.direction_current == Direction.right:
                distance_traveled = batman.x_current - batman.x_previous

                x_start = batman.x_previous + distance_traveled // 2 + 1

                self.map[self.usable_y_min:self.usable_y_max, self.usable_x_min:x_start] = -1
                self.usable_x_min = x_start

            else:
                # if last direction is one of up_right, up_left, down_right, down_left do not update the map
                pass

        elif bomb_distance == "COLDER":
            if batman.direction_current == Direction.down:
                distance_traveled = batman.y_current - batman.y_previous

                y_end = batman.y_current - distance_traveled // 2

                self.map[y_end:self.usable_y_max, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_max = y_end

            elif batman.direction_current == Direction.up:
                distance_traveled = batman.y_previous - batman.y_current

                y_start = batman.y_current + distance_traveled // 2 + 1

                self.map[self.usable_y_min:y_start, self.usable_x_min:self.usable_x_max] = -1
                self.usable_y_min = y_start

            elif batman.direction_current == Direction.left:
                distance_traveled = batman.x_previous - batman.x_current

                x_start = batman.x_current + distance_traveled // 2 + 1

                self.map[self.usable_y_min:self.usable_y_max, self.usable_x_min:x_start] = -1
                self.usable_x_min = x_start

            elif batman.direction_current == Direction.right:
                distance_traveled = batman.x_current - batman.x_previous

                x_end = batman.x_current - distance_traveled // 2

                self.map[self.usable_y_min:self.usable_y_max, x_end:self.usable_x_max] = -1
                self.usable_x_max = x_end

            else:
                # if last direction is one of up_right, up_left, down_right, down_left do not update the map
                pass
        else:   # UNKNOWN
            pass

        print("self.usable_x_min: " + str(self.usable_x_min), file=sys.stderr)
        print("self.usable_x_max: " + str(self.usable_x_max), file=sys.stderr)
        print("self.usable_y_min: " + str(self.usable_y_min), file=sys.stderr)
        print("self.usable_y_max: " + str(self.usable_y_max), file=sys.stderr)

    def check_if_only_one_column_left(self):
        usable_x_width = self.usable_x_max - self.usable_x_min

        if usable_x_width == 1:
            return True
        else:
            return False

    def check_if_only_one_row_left(self):
        usable_y_width = self.usable_y_max - self.usable_y_min

        if usable_y_width == 1:
            return True
        else:
            return False

    def check_if_only_one_cell_left(self):
        usable_x_width = self.usable_x_max - self.usable_x_min
        usable_y_width = self.usable_y_max - self.usable_y_min

        if usable_x_width == 1 and usable_y_width == 1:
            return True
        else:
            return False

    def find_next_position_new(self, current_x, current_y, movement):

        usable_y_midpoint = (self.usable_y_max + self.usable_y_min) // 2
        usable_x_midpoint = (self.usable_x_max + self.usable_x_min) // 2

        print("Midpoint x: " + str(usable_x_midpoint) + ", y: " + str(usable_y_midpoint), file=sys.stderr)

        if movement == Movements.vertical:
            if current_y < usable_y_midpoint:
                if current_y < self.usable_y_min:
                    new_y = self.usable_y_min
                else:
                    new_y = (self.usable_y_max - 1) - (current_y - self.usable_y_min)
            else:
                if current_y > self.usable_y_max:
                    new_y = self.usable_y_max - 1
                else:
                    new_y = max(self.usable_y_min + ((self.usable_y_max - 1) - current_y), self.usable_y_min)

            print("New y: " + str(new_y), file=sys.stderr)

            return current_x, new_y
        elif movement == Movements.horizontal:
            if current_x < usable_x_midpoint:
                new_x = (self.usable_x_max - 1) - (current_x - self.usable_x_min)
            else:
                new_x = self.usable_x_min + ((self.usable_x_max - 1) - current_x)

            print("New x: " + str(new_x), file=sys.stderr)

            return new_x, current_y
        else:
            return self.usable_x_max-1, self.usable_y_max-1


class Batman:
    def __init__(self, x0, y0):
        self.x_current = x0
        self.y_current = y0

        self.x_previous = x0
        self.y_previous = y0

        self.movement = Movements.vertical

        self.direction_current = Direction.up

        self.vertical_distance = "UNKNOWN"
        self.horizontal_distance = "UNKNOWN"

    def update_movement(self, current_distance):

        if current_distance != "UNKNOWN":
            if self.movement == Movements.vertical:
                self.vertical_distance = current_distance
                self.movement = Movements.horizontal
            elif self.movement == Movements.horizontal:
                self.horizontal_distance = current_distance
                if self.vertical_distance == "WARMER" and self.horizontal_distance == "WARMER":
                    self.movement = Movements.vertical
                else:
                    self.movement = Movements.mixed
            else:   # UNKNOWN
                self.movement = Movements.vertical
        else:
            pass

    def set_movement(self, new_movement):
        self.movement = new_movement

    def set_position(self, x, y):
        self.x_previous = self.x_current
        self.y_previous = self.y_current

        self.x_current = x
        self.y_current = y

        self.__update_direction()

    def __update_direction(self):
        # this could be decided based on self. movement, but this method is more general
        if self.x_current == self.x_previous:
            # vertical
            if self.y_current < self.y_previous:
                self.direction_current = Direction.up
            else:
                self.direction_current = Direction.down
        elif self.y_current == self.y_previous:
            # horizontal
            if self.x_current < self.x_previous:
                self.direction_current = Direction.left
            else:
                self.direction_current = Direction.right
        else:
            # mixed direction
            self.direction_current = Direction.mixed

    def get_as_string(self):
        r = "Batman: \n"
        r += "x: " + str(self.x_current) + ", y: " + str(self.y_current) + "\n"
        r += "x_p: " + str(self.x_previous) + ", y_p: " + str(self.y_previous) + "\n"
        r += "dir: " + str(self.direction_current) + "\n"
        r += "dis_vertical: " + str(self.vertical_distance) + ", dis_horizontal: " + str(self.horizontal_distance) + "\n"
        r += "movement: " + str(self.movement)

        return r

if __name__ == '__main__':

    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]

    print("w: " + str(w) + ", h: " + str(h), file=sys.stderr)

    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]

    building = Building(w, h)
    batman = Batman(x0, y0)

    # game loop
    while 1:
        bomb_dist = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)

        batman.update_movement(bomb_dist)

        print(batman.get_as_string(), file=sys.stderr)

        building.update_map(batman, bomb_dist)

        if building.check_if_only_one_cell_left():
            batman.set_position(building.usable_x_min, building.usable_y_min)
        else:
            if building.check_if_only_one_column_left():
                batman.set_movement(Movements.vertical)
            if building.check_if_only_one_row_left():
                batman.set_movement(Movements.horizontal)

            #print(building.map, file=sys.stderr)

            batman_new_x, batman_new_y = building.find_next_position_new(batman.x_current, batman.y_current, batman.movement)
            batman.set_position(batman_new_x, batman_new_y)

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        print(str(batman.x_current) + " " + str(batman.y_current))
