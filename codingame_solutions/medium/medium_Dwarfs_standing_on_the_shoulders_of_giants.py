__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math
import itertools

from codingame_solutions.utilities.graph import Graph


graph = Graph()

n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]

    graph.add_edge((x, y))

print(graph, file=sys.stderr)

vertices_pairs = itertools.permutations(graph.vertices(), 2)

paths = []
for vertices_pair in vertices_pairs:
    print("vertices_pair: " + str(vertices_pair), file=sys.stderr)
    new_paths = graph.find_all_paths(vertices_pair[0], vertices_pair[1])
    paths += new_paths

print("Paths: " + str(paths), file=sys.stderr)

longest_path_length = max([len(l) for l in paths])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# The number of people involved in the longest succession of influences
print(longest_path_length)
