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


def calculate_number_of_points_further(building):
    number_of_points_further = 0
    number_of_points_same = 0

    for i in range(building.height):
        for j in range(building.width):
            if building.map[i][j] == -1:
                number_of_points_further += 1
            elif building.map[i][j] == 3:
                number_of_points_same += 1

    if number_of_points_further != 0 or number_of_points_same != 0:
        print("number_of_points_same: " + str(number_of_points_same))
        print("number_of_points_further: " + str(number_of_points_further))


def find_best_spot(building_staring):
    building_test = Building(building_staring.width, building_staring.height)
    for i in range(building_staring.height//2 + 1):
        for j in range(building_staring.width):
            calculate_distances(j, i, building_test)
            building_result = compare_distances(building_staring, building_test)
            building_result.map[building_result.width//2:][:] = 0
            print("x: " + str(j) + ", y: " + str(i))
            calculate_number_of_points_further(building_result)


if __name__ == '__main__':
    np.set_printoptions(precision=2)

    width = 24
    height = 6

    building_previous = Building(width, height)
    building_current = Building(width, height)

    x, y = [int(v) for v in input().split()]

    batman = Batman(x, y)
    calculate_distances(batman.x_current, batman.y_current, building_previous)

    #find_best_spot(building_previous)

    x, y = [int(v) for v in input().split()]
    new_x, new_y = x, y

    batman.set_position(new_x, new_y)
    calculate_distances(batman.x_current, batman.y_current, building_current)

    building_result = compare_distances(building_previous, building_current)
    building_result.map[height//2:][:] = 0
    building_result.map[new_y][new_x] = 9

    print(building_result.map)
