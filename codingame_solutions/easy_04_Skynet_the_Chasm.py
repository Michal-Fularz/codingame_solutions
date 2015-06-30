__author__ = 'Amin'

import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input())  # the length of the road before the gap.
gap = int(raw_input())  # the length of the gap.
platform = int(raw_input())  # the length of the landing platform.

required_speed = gap + 1

# game loop
while 1:
    speed = int(raw_input())  # the motorbike's speed.
    coordX = int(raw_input())  # the position on the road of the motorbike.

    action = ""

    # decide if we are before or after the gap
    if coordX < road:
        if (coordX + speed) > road:
            action = "JUMP"
        else:
            if speed < required_speed:
                action = "SPEED"
            elif speed > required_speed:
                action = "SLOW"
            else:
                action = "WAIT"
    else:
        action = "SLOW"

    print >> sys.stderr, "Choosen action: " + action


    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print action # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.