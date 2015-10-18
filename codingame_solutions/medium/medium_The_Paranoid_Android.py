__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math


class Floor:
    def __init__(self, width, contains_exit=False, exit_position=-1):
        self.width = width
        self.__contains_elevator = False
        self.__elevator_position = -1
        self.__contains_exit = contains_exit
        self.__exit_position = exit_position

    def add_exit(self, exit_position):
        self.__contains_exit = True
        self.__exit_position = exit_position

    def add_elevator(self, elevator_position):
        self.__contains_elevator = True
        self.__elevator_position = elevator_position

    def should_be_blocked(self, position, direction):
        flag_should_be_blocked = False

        if self.__contains_elevator:
            if position > self.__elevator_position and direction == "RIGHT" or \
                    position < self.__elevator_position and direction == "LEFT":
                flag_should_be_blocked = True
        elif self.__contains_exit:
            if position > self.__exit_position and direction == "RIGHT" or \
                    position < self.__exit_position and direction == "LEFT":
                flag_should_be_blocked = True

        return flag_should_be_blocked


class Drive:
    def __init__(self):
        self.floors = []

        self.load_from_input()

    def load_from_input(self):
        # nb_floors: number of floors
        # width: width of the area
        # nb_rounds: maximum number of rounds
        # exit_floor: floor on which the exit is found
        # exit_pos: position of the exit on its floor
        # nb_total_clones: number of generated clones
        # nb_additional_elevators: ignore (always zero)
        # nb_elevators: number of elevators
        nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]

        for i in xrange(nb_floors):
            self.floors.append(Floor(width))

        self.floors[exit_floor].add_exit(exit_pos)

        for i in xrange(nb_elevators):
            # elevator_floor: floor on which this elevator is found
            # elevator_pos: position of the elevator on its floor
            elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
            self.floors[elevator_floor].add_elevator(elevator_pos)


# MAIN

drive = Drive()

flag_do_the_blocking = False

# game loop
while 1:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    flag_do_the_blocking = drive.floors[clone_floor].should_be_blocked(clone_pos, direction)

    # action: WAIT or BLOCK
    if flag_do_the_blocking:
        print "BLOCK"
    else:
        print "WAIT"
