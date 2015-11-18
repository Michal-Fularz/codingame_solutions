__author__ = 'Amin'

import sys
import math

from codingame_solutions.utilities.graph import Graph, GraphEdge


if __name__ == "__main__":

    f = open("hard_Bender_The_Money_Machine/test06_in.txt")

    n = int(f.readline())
    n = int(input())

    v_names = []
    v_values = []
    v_destination_1 = []
    v_destination_2 = []

    for i in range(n):
        room = f.readline()
        room = input()
        vertex_name, vertex_value, vertex_neighbour_1, vertex_neighbour_2 = [v for v in room.split()]
        v_names.append(int(vertex_name))
        v_values.append(int(vertex_value))
        if vertex_neighbour_1 != "E":
            v_destination_1.append(int(vertex_neighbour_1))
        else:
            v_destination_1.append(-1)
        if vertex_neighbour_2 != "E":
            v_destination_2.append(int(vertex_neighbour_2))
        else:
            v_destination_2.append(-1)

    # create graph
    g = Graph(flag_dag=True)

    for name in v_names:
        g.add_vertex(name)
        if v_destination_1[name] != -1:
            g.add_edge(GraphEdge(name, v_destination_1[name], v_values[v_destination_1[name]]))
        if v_destination_2[name] != -1:
            g.add_edge(GraphEdge(name, v_destination_2[name], v_values[v_destination_2[name]]))

    #print(g.edges(), file=sys.stderr)
    #print(g.vertices(), file=sys.stderr)
    #print(g.find_longest_path(0), file=sys.stderr)

    max_dist = max([value for key, value in g.find_longest_path(0).items()]) + v_values[0]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(max_dist)
