__author__ = 'Amin'

import sys
import math
import numpy as np
from enum import Enum

from codingame_solutions.very_hard.very_hard_Triangulation import Batman
from codingame_solutions.very_hard.very_hard_Triangulation import Building


def calculate_distances(x, y, building):
    for i in range(building.height):
        for j in range(building.width):
            building.map[i][j] = math.sqrt((i-y)**2 + (j-x)**2)


def compare_distances(building_1, buidling_2):
    building_result = Building(building_1.width, building_1.height)

    for i in range(building_1.height):
        for j in range(building_1.width):
            if building_1.map[i][j] > buidling_2.map[i][j]:
                building_result.map[i][j] = 1
            elif building_1.map[i][j] < buidling_2.map[i][j]:
                building_result.map[i][j] = -1
            else:
                building_result.map[i][j] = 3

    return building_result

if __name__ == '__main__':
    np.set_printoptions(precision=2)

    width = 11
    height = 11

    building_previous = Building(width, height)
    building_current = Building(width, height)

    batman = Batman(5, 10)
    calculate_distances(batman.x_current, batman.y_current, building_previous)

    new_x, new_y = 0, 10

    batman.set_position(new_x, new_y)
    calculate_distances(batman.x_current, batman.y_current, building_current)

    building_result = compare_distances(building_previous, building_current)
    building_result.map[5:][:] = 0
    building_result.map[new_y][new_x] = 9

    print(building_result.map)
