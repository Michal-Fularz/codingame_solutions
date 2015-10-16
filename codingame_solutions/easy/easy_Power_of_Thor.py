__author__ = 'Amin'

import sys
import math


# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

current_tx = initial_tx
current_ty = initial_ty

# game loop
while 1:
    remaining_turns = int(raw_input())

    direction = ""
    if current_ty > light_y:
        direction += "N"
        current_ty -= 1
    if current_ty < light_y:
        direction += "S"
        current_ty += 1
    if current_tx > light_x:
        direction += "W"
        current_tx -= 1
    if current_tx < light_x:
        direction += "E"
        current_tx += 1

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print direction
