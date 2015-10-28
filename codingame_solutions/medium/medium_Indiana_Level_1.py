__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math
from enum import Enum


class Direction(Enum):
    top = 1
    bottom = 2
    left = 3
    right = 4
    na = 5
    
    def get_from_text(text):
        direction = Direction.na
        if text == "TOP":
            direction = Direction.top
        elif text == "LEFT":
            direction = Direction.left
        elif text == "RIGHT":
            direction = Direction.right
        else:
            print("Wrong direction text!", file=sys.stderr)
        
        return direction


class EntryExit:
    def __init__(self, entry: Direction, exit):
        self.entry = entry
        self.exit = exit
        

class Room:
    def __init__(self, type=0):
        self.type = type
        self.paths = []
        self.__create_paths()
        
    def __create_paths(self):
        if self.type == 0:
            # no entries, no exits
            pass
        elif self.type == 1:
            self.paths.append(EntryExit(Direction.top, Direction.bottom))
            self.paths.append(EntryExit(Direction.left, Direction.bottom))
            self.paths.append(EntryExit(Direction.right, Direction.bottom))
        elif self.type == 2:
            self.paths.append(EntryExit(Direction.left, Direction.right))
            self.paths.append(EntryExit(Direction.right, Direction.left))
        elif self.type == 3:
            self.paths.append(EntryExit(Direction.top, Direction.bottom))
        elif self.type == 4:
            self.paths.append(EntryExit(Direction.top, Direction.left))
            self.paths.append(EntryExit(Direction.right, Direction.bottom))
        elif self.type == 5:
            self.paths.append(EntryExit(Direction.top, Direction.right))
            self.paths.append(EntryExit(Direction.left, Direction.bottom))
        elif self.type == 6:
            self.paths.append(EntryExit(Direction.top, Direction.na))
            self.paths.append(EntryExit(Direction.left, Direction.right))
            self.paths.append(EntryExit(Direction.right, Direction.left))
        elif self.type == 7:
            self.paths.append(EntryExit(Direction.top, Direction.bottom))
            self.paths.append(EntryExit(Direction.right, Direction.bottom))
        elif self.type == 8:
            self.paths.append(EntryExit(Direction.left, Direction.bottom))
            self.paths.append(EntryExit(Direction.right, Direction.bottom))
        elif self.type == 9:
            self.paths.append(EntryExit(Direction.top, Direction.bottom))
            self.paths.append(EntryExit(Direction.left, Direction.bottom))
        elif self.type == 10:
            self.paths.append(EntryExit(Direction.top, Direction.left))
            self.paths.append(EntryExit(Direction.left, Direction.na))
        elif self.type == 11:
            self.paths.append(EntryExit(Direction.top, Direction.right))
            self.paths.append(EntryExit(Direction.right, Direction.na))
        elif self.type == 12:
            self.paths.append(EntryExit(Direction.right, Direction.bottom))
        elif self.type == 13:
            self.paths.append(EntryExit(Direction.left, Direction.bottom))
        else:
            print("Wrong room type!", file=sys.stderr)
            
    def get_exit(self, entry):
        exit = Direction.na
        
        for path in self.paths:
            if path.entry == entry:
                exit = path.exit
        
        return exit

            
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rooms = []
        
        self.__read_from_input()
    
    def __read_from_input(self):
        for i in range(self.height):
            row_of_rooms = []
            line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
            values = [int(x) for x in line.split()]
            for value in values:
                row_of_rooms.append(Room(value))
            self.rooms.append(row_of_rooms)
            
    def get_as_string(self):
        r = ""
        r += "Width: " + str(self.width) + ", height: " + str(self.height) + "\n"
        for row_of_rooms in self.rooms:
            for room in row_of_rooms:
                r += str(room.type) + ", "
            r += "\n"
        return r
        
    def get_exit_of_room_entered(self, x: int, y: int, direction: Direction):
        return self.rooms[y][x].get_exit(direction)
        

class Indy:
    def __init__(self):
        self.position_x = -1
        self.position_y = -1
        self.direction = Direction.na
        
    def set(self, position_x: int, position_y: int, direction: str):
        self.position_x = position_x
        self.position_y = position_y
        self.direction = Direction.get_from_text(direction)
        
    def get_next_position(self, board: Board):
        next_direction = board.get_exit_of_room_entered(self.position_x, self.position_y, self.direction)
        
        if next_direction == Direction.bottom:
            next_position_x = self.position_x
            next_position_y = self.position_y + 1
        elif next_direction == Direction.right:
            next_position_x = self.position_x + 1
            next_position_y = self.position_y
        elif next_direction == Direction.left:
            next_position_x = self.position_x - 1
            next_position_y = self.position_y
        else:
            next_position_x = -1
            next_position_y = -1
            print("Wrong next direction: " + str(next_direction), file=sys.stderr)
        
        return next_position_x, next_position_y
        

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
b = Board(w, h)
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

print(b.get_as_string(), file=sys.stderr)

hero = Indy()

# game loop
while 1:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    hero.set(xi, yi, pos)
    next_xi, next_yi = hero.get_next_position(b)
    print("Next position: " + str(next_xi) + ", " + str(next_yi), file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    r = str(next_xi) + " " + str(next_yi)
    print(r)
