__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

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

        self.map = np.zeros((self.height, self.width))  # , dtype=np.uint8)

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


class BuildingOld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Width: " + str(self.width) + ", height: " + str(self.height), file=sys.stderr)

        self.map = np.zeros((self.height, self.width))  # , dtype=np.uint8)
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


class BatmanOld:
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


if __name__ == '__main__':

    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]

    print("w: " + str(w) + ", h: " + str(h), file=sys.stderr)

    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]

    if w != 8000 and h != 8000:
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

    else:
        building = BuildingOld(w, h)
        batman = BatmanOld(x0, y0)

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
