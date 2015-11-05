__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math
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

#print(persons, file=sys.stderr)

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

result = set(longest_paths[0])
for s in longest_paths[1:]:
    result.intersection_update(s)
print("result: " + str(result), file=sys.stderr)

# analyze all the common elements
paths = persons.find_all_paths_from_vertex(list(result)[-1])
longest_path_length = max([len(l) for l in paths])
minimal_distance = longest_path_length

minimal_distance = 9999
for person_name in list(result):
    paths = persons.find_all_paths_from_vertex(person_name)
    longest_path_length = max([len(l) for l in paths])
    print("longest_path_length: " + str(longest_path_length), file=sys.stderr)
    if longest_path_length < minimal_distance:
        minimal_distance = longest_path_length

# other (much slower) solutions:
# iterate over every node of each path in longest_paths

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# The minimal amount of steps required to completely propagate the advertisement
print(minimal_distance-1)
