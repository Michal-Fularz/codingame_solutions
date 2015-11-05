import sys
import math

import numpy as np
from codingame_solutions.utilities.graph import Graph


# MAIN

persons = Graph()

n = int(input())  # the number of adjacency relations
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]

    persons.add_edge((xi, yi))
    persons.add_edge((yi, xi))

print(persons, file=sys.stderr)

solution = 2

if solution == 1:
    # lets start with first person that has one neighbour
    persons_with_1_neighbour = persons.get_vertices_with_n_edges(1)
    print("persons_with_1_neighbour: " + str(persons_with_1_neighbour), file=sys.stderr)

    paths = persons.find_all_paths_from_vertex(persons_with_1_neighbour[0])
    print("paths: " + str(paths), file=sys.stderr)

    longest_path_length = max([len(l) for l in paths])

    longest_paths = []
    for path in paths:
        if len(path) == longest_path_length:
            longest_paths.append(path)
    print("longest_paths: " + str(longest_paths), file=sys.stderr)

    minimal_distance = 9999
    for path in longest_paths:
        for person_name in path:
            paths = persons.find_all_paths_from_vertex(person_name)
            longest_path_length = max([len(l) for l in paths])
            print("longest_path_length: " + str(longest_path_length), file=sys.stderr)
            if longest_path_length < minimal_distance:
                minimal_distance = longest_path_length

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The minimal amount of steps required to completely propagate the advertisement
    print(minimal_distance-1)

elif solution == 2:
    number_of_vertices = len(persons.vertices())
    print("number_of_vertices: " + str(number_of_vertices), file=sys.stderr)
    neighbourhood = np.zeros((number_of_vertices, number_of_vertices), dtype=int)
    print("neighbourhood: \n" + str(neighbourhood), file=sys.stderr)

    node_name_to_index = []

    for edge in persons.edges():
        print("edge: " + str(edge), file=sys.stderr)
        v = list(edge)

        # TODO: conversion between edge name and index is necessary

        if v[0] in node_name_to_index:
            index_1 = node_name_to_index.index(v[0])
        else:
            index_1 = len(node_name_to_index)
            node_name_to_index.append(v[0])

        if v[1] in node_name_to_index:
            index_2 = node_name_to_index.index(v[1])
        else:
            index_2 = len(node_name_to_index)
            node_name_to_index.append(v[1])

        if index_1 > index_2:
            existing_element_index, new_element_index = index_2, index_1
        else:
            existing_element_index, new_element_index = index_1, index_2

        print("existing_element_index: " + str(existing_element_index), file=sys.stderr)
        print("new_element_index: " + str(new_element_index), file=sys.stderr)


        neighbourhood[existing_element_index][new_element_index] = 1
        neighbourhood[new_element_index][existing_element_index] = 1

        # fill the new column
        for i in range(new_element_index):
            if i != existing_element_index:
                neighbourhood[i][new_element_index] = neighbourhood[i][existing_element_index] + 1

        # fill the new row
        for j in range(new_element_index):
            if j != existing_element_index:
                neighbourhood[new_element_index][j] = neighbourhood[existing_element_index][j] + 1

    print("neighbourhood: \n" + str(neighbourhood), file=sys.stderr)

    # find max in each row
    maximums = [max(c) for c in neighbourhood[:]]
    print("maximums: \n" + str(maximums), file=sys.stderr)

    minimal_distance = min(maximums)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The minimal amount of steps required to completely propagate the advertisement
    print(minimal_distance)
