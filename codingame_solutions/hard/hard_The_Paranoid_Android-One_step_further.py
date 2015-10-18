__author__ = 'Amin'

import sys
import math


class Floor:
    def __init__(self, width):
        self.width = width
        self.contains_elevator = False
        self.elevators_positions = []
        self.contains_exit = False
        self.exit_position = -1

    def add_exit(self, exit_position):
        self.contains_exit = True
        self.exit_position = exit_position

    def add_elevator(self, elevator_position):
        self.contains_elevator = True
        self.elevators_positions.append(elevator_position)

    def should_be_blocked(self, position, direction):
        flag_should_be_blocked = False
        flag_should_build_elevator = False

        if self.contains_elevator:
            if position > self.__elevator_position and direction == "RIGHT" or \
                    position < self.__elevator_position and direction == "LEFT":
                flag_should_be_blocked = True
        elif self.contains_exit:
            if position > self.exit_position and direction == "RIGHT" or \
                    position < self.exit_position and direction == "LEFT":
                flag_should_be_blocked = True
        else:
            flag_should_build_elevator = True

        return flag_should_be_blocked, flag_should_build_elevator


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
        # nb_additional_elevators: number of additional elevators that you can build
        # nb_elevators: number of elevators
        nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = \
            [int(i) for i in input().split()]

        for i in range(nb_floors):
            self.floors.append(Floor(width))

        self.floors[exit_floor].add_exit(exit_pos)

        for i in range(nb_elevators):
            # elevator_floor: floor on which this elevator is found
            # elevator_pos: position of the elevator on its floor
            elevator_floor, elevator_pos = [int(j) for j in input().split()]
            self.floors[elevator_floor].add_elevator(elevator_pos)


# TODO: find all the available paths to the elevator, calculate the distance, and number of clones required
class Path:
    def __init__(self):
        pass


# MAIN

drive = Drive()

flag_do_the_blocking = False

# game loop
while 1:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    flag_do_the_blocking, flag_build_elevator = drive.floors[clone_floor].should_be_blocked(clone_pos, direction)

    # action: WAIT or BLOCK or ELEVATOR
    if flag_do_the_blocking:
        print("BLOCK")
    elif flag_build_elevator:
        print("ELEVATOR")
        drive.floors[clone_floor].add_elevator(clone_pos)
    else:
        print("WAIT")
