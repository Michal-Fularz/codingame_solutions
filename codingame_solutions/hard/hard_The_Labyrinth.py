__author__ = 'Amin'

import sys
import math

function A*(start,goal)
    ClosedSet := {}    	  // The set of nodes already evaluated.
    OpenSet := {start}    // The set of tentative nodes to be evaluated, initially containing the start node
    Came_From := the empty map    // The map of navigated nodes.

    g_score := map with default value of Infinity
    g_score[start] := 0    // Cost from start along best known path.
    // Estimated total cost from start to goal through y.
    f_score := map with default value of Infinity
    f_score[start] := g_score[start] + heuristic_cost_estimate(start, goal)

    while OpenSet is not empty
        current := the node in OpenSet having the lowest f_score[] value
        if current = goal
            return reconstruct_path(Came_From, goal)

        OpenSet.Remove(current)
        ClosedSet.Add(current)
        for each neighbor of current
            if neighbor in ClosedSet
                continue		// Ignore the neighbor which is already evaluated.
            tentative_g_score := g_score[current] + dist_between(current,neighbor) // length of this path.
            if neighbor not in OpenSet	// Discover a new node
                OpenSet.Add(neighbor)
            else if tentative_g_score >= g_score[neighbor]
                continue		// This is not a better path.

            // This path is the best until now. Record it!
            Came_From[neighbor] := current
            g_score[neighbor] := tentative_g_score
            f_score[neighbor] := g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)

    return failure

function reconstruct_path(Came_From,current)
    total_path := [current]
    while current in Came_From.Keys:
        current := Came_From[current]
        total_path.append(current)
    return total_path

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

# game loop
while 1:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Kirk's next move (UP DOWN LEFT or RIGHT).
    print("RIGHT")

