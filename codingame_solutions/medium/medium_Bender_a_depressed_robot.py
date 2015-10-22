__author__ = 'Amin'

import sys
import math
from enum import Enum


class Direction(Enum):
    south = 1
    east = 2
    north = 3
    west = 4

    def get_as_string(self):
        r = ""
        if self == Direction.south:
            r = "SOUTH"
        elif self == Direction.north:
            r = "NORTH"
        elif self == Direction.east:
            r = "EAST"
        elif self == Direction.west:
            r = "WEST"
        else:
            r = "WRONG VALUE"

        return r


class Bender:
    def __init__(self, starting_point_x: int, starting_point_y: int):
        self.current_position = (starting_point_x, starting_point_y)
        self.current_direction = Direction.south

        self.__priorities = [Direction.south, Direction.east, Direction.north, Direction.west]
        self.__priorities_inverted = [Direction.west, Direction.north, Direction.east, Direction.south]

        self.flag_breaker_mode = False
        self.flag_inverted_mode = False

    def change_direction2(self):
        if self.flag_inverted_mode:
            priorities = self.__priorities_inverted
        else:
            priorities = self.__priorities

        current_direction_index = self.__priorities.index(self.current_direction)

        current_direction_index += 1
        if current_direction_index >= len(priorities):
            current_direction_index = 0

        self.current_direction = priorities[current_direction_index]

    def change_direction(self, cell_down, cell_up, cell_left, cell_right):

        print("cell_down" + str(cell_down), file=sys.stderr)
        print("cell_up" + str(cell_up), file=sys.stderr)
        print("cell_left" + str(cell_left), file=sys.stderr)
        print("cell_right" + str(cell_right), file=sys.stderr)

        if not self.flag_inverted_mode:
            if cell_down != "#" and (cell_down != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.south
            elif cell_right != "#" and (cell_right != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.east
            elif cell_up != "#" and (cell_up != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.north
            elif cell_left != "#" and (cell_left != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.west
        else:
            if cell_left != "#" and (cell_left != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.west
            elif cell_up != "#" and (cell_up != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.north
            elif cell_right != "#" and (cell_right != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.east
            elif cell_down != "#" and (cell_down != "X" or self.flag_breaker_mode):
                self.current_direction = Direction.south

    def set_direction(self, direction: str):
        if direction == "S":
            self.current_direction = Direction.south
        elif direction == "N":
            self.current_direction = Direction.north
        elif direction == "E":
            self.current_direction = Direction.east
        elif direction == "W":
            self.current_direction = Direction.west

    def get_next_position(self):
        next_x = -1
        next_y = -1

        if self.current_direction == Direction.south:
            next_x = self.current_position[0]
            next_y = self.current_position[1] + 1
        elif self.current_direction == Direction.north:
            next_x = self.current_position[0]
            next_y = self.current_position[1] - 1
        elif self.current_direction == Direction.east:
            next_x = self.current_position[0] + 1
            next_y = self.current_position[1]
        elif self.current_direction == Direction.west:
            next_x = self.current_position[0] - 1
            next_y = self.current_position[1]
        else:
            pass

        return next_x, next_y

    def move(self, x: int, y: int):
        self.current_position = (x, y)

    def change_priorities(self):
        self.flag_inverted_mode = not self.flag_inverted_mode


class FuturamaCity:
    def __init__(self):
        self.map = []
        self.width = -1
        self.height = -1

        self.__load_from_input()

    def __load_from_input(self):
        self.height, self.width = [int(i) for i in input().split()]
        for i in range(self.height):
            row = input()

            map_row = []
            # do not take into account first and last column
            for character in row:
                map_row.append(character)
            self.map.append(map_row)

    def get_map(self):
        r = ""
        for row in self.map:
            for character in row:
                r += character
            r += "\n"

        return r

    def find_starting_point(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] == "@":
                    return j, i

        return -1, -1

    def get_cell(self, x: int, y: int):
        return self.map[y][x]

    def check_if_in_range(self, x: int, y: int):
        flag_in_range = True
        if x < 0 or x >= self.width:
            flag_in_range = False
        if y < 0 or y >= self.height:
            flag_in_range = False

        return flag_in_range

    def remove_bear(self, x: int, y: int):
        self.map[y][x] = " "


f = FuturamaCity()
print("Map:", file=sys.stderr)
print(f.get_map(), file=sys.stderr)

x, y = f.find_starting_point()
b = Bender(x, y)
print("Bender start: " + str(x) + ", " + str(y), file=sys.stderr)

moves = []
flag_game_is_on = True
while flag_game_is_on:
    print("Bender: " + str(b.current_position[0]) + ", " + str(b.current_position[1]) + ", " + str(b.current_direction), file=sys.stderr)

    next_x, next_y = b.get_next_position()
    cell = f.get_cell(next_x, next_y)

    if cell == "#" or (cell == "X" and not b.flag_breaker_mode):
        cell_down = f.get_cell(b.current_position[0], b.current_position[1]+1)
        cell_up = f.get_cell(b.current_position[0], b.current_position[1]-1)
        cell_left = f.get_cell(b.current_position[0]-1, b.current_position[1])
        cell_right = f.get_cell(b.current_position[0]+1, b.current_position[1])

        b.change_direction(cell_down, cell_up, cell_left, cell_right)
    else:
        b.move(next_x, next_y)
        moves.append(b.current_direction)

        if cell == "$":
            flag_game_is_on = False
        elif cell == "X" and b.flag_breaker_mode:
            pass
        elif cell == "S" or cell == "N" or cell == "E" or cell == "W":
            b.set_direction(cell)
        elif cell == "I":
            b.change_priorities()
        elif cell == "B":
            if b.flag_breaker_mode:
                b.flag_breaker_mode = False
            else:
                b.flag_breaker_mode = True
                f.remove_bear(next_x, next_y)
        elif cell == "T":
            print("Teleports not implemented yet", file=sys.stderr)
        elif cell == " ":
            pass
        elif cell == "@":
            pass
        else:
            print("Wrong cell value!", file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

r = ""
for move in moves:
    r += move.get_as_string()
    r += "\n"

print(r[:-1])
