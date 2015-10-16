__author__ = 'Amin'

import sys
import math

previous_space_y = 0
flag_fired_this_turn = False

# game loop
while 1:
    space_x, space_y = [int(i) for i in raw_input().split()]

    if previous_space_y != space_y:
        previous_space_y = space_y
        flag_fired_this_turn = False

    action = "HOLD"

    highest_mountain_height = 0
    highest_mountain_index = 0
    for i in xrange(8):
        mountain_h = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.

        if mountain_h > highest_mountain_height:
            highest_mountain_height = mountain_h
            highest_mountain_index = i

    if space_x == highest_mountain_index and not flag_fired_this_turn:
        flag_fired_this_turn = True
        action = "FIRE"

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
    print action
