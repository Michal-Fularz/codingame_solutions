__author__ = 'Amin'

import sys
import math


class Person:
    def __init__(self, name):
        self.neighbours = []
        self.was_visited = False
        self.__name = name

    def add_neighbour(self, new_neighbour):
        self.neighbours.append(new_neighbour)

    def mark_as_visited(self):
        self.was_visited = True

    def mark_as_not_visited(self):
        self.was_visited = False

    def get_name(self):
        return self.__name


def propagate(current_person, persons, existing_nodes, recurse=True):
    depth = 1
    visited_nodes = [current_person.get_name()]
    current_person.mark_as_visited()

    depths = []
    lst_visited_nodes = []

    for neighbour in current_person.neighbours:
        if not persons[neighbour].was_visited:
            d, vn = propagate(persons[neighbour], persons, existing_nodes)
            depths.append(d)
            lst_visited_nodes.append(vn)

    if recurse:
        if len(depths) > 0:
            max_depth = -1
            max_depth_index = -1
            for i in xrange(len(depths)):
                if depths[i] > max_depth:
                    max_depth = depths[i]
                    max_depth_index = i

            depth += depths[max_depth_index]
            visited_nodes += lst_visited_nodes[max_depth_index]

        return depth, visited_nodes

    else:
        return depths, lst_visited_nodes

    #if len(depths) > 0:
        #depth += max(depths)



# MAIN

persons = []
existing_nodes = []
number_of_nodes = 0

n = int(raw_input())    # the number of adjacency relations

for i in xrange(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in raw_input().split()]

    # check if any of the persons is in the set

    if xi not in existing_nodes:
        existing_nodes.append(xi)
        persons.append(Person(existing_nodes.index(xi)))
        number_of_nodes += 1

    if yi not in existing_nodes:
        existing_nodes.append(yi)
        persons.append(Person(existing_nodes.index(yi)))
        number_of_nodes += 1

    persons[existing_nodes.index(xi)].add_neighbour(existing_nodes.index(yi))
    persons[existing_nodes.index(yi)].add_neighbour(existing_nodes.index(xi))

for person in persons:
    n = ""
    for neigh in person.neighbours:
        n += str(neigh) + ", "
    print >> sys.stderr, str(person.get_name()) + ", neigh: " + n

for node in existing_nodes:
    print >> sys.stderr, "Nodes: " + str(node)

flag_continue = True

# lets start with first person
depths = []
lst_visited_nodes = []
depths, lst_visited_nodes = propagate(persons[0], persons, existing_nodes, recurse=False)

current_depth = 999
previous_depth = 999

while flag_continue:
    longest_path = 0
    nodes_on_longest_path = []

    if len(depths) == 1:
        longest_path = depths[0]
        nodes_on_longest_path = lst_visited_nodes[0]

    else:
        max_depth = -1
        max_depth_index = -1
        for i in xrange(len(depths)):
            if depths[i] > max_depth:
                max_depth = depths[i]
                max_depth_index = i

        longest_path += depths[max_depth_index]
        nodes_on_longest_path += lst_visited_nodes[max_depth_index]

    #difference_between_longest_paths = longest_path
    #number_of_nodes_to_move = difference_between_longest_paths // 2
    # for node in nodes_on_longest_path:
    #     print >> sys.stderr, "lst of nodes: " + str(node)
    # for d in depths:
    #     print >> sys.stderr, "depth: " + str(d)
    # print >> sys.stderr, "diff: " + str(difference_between_longest_paths)
    # print >> sys.stderr, "number: " + str(number_of_nodes_to_move)
    # index_of_best_node = nodes_on_longest_path[number_of_nodes_to_move-1]
    index_of_best_node = nodes_on_longest_path[0]

    for person in persons:
        person.mark_as_not_visited()

    depths, lst_visited_nodes = propagate(persons[index_of_best_node], persons, existing_nodes, recurse=False)



    if max(depths) >= previous_depth:
        current_depth = previous_depth
        flag_continue = False
    else:
        previous_depth = current_depth
        current_depth = max(depths)

    print >> sys.stderr, "final depth: " + str(max(depths)-1)

# for depth in depths:
#     print >> sys.stderr, "Depth: " + str(depth)

# The minimal amount of steps required to completely propagate the advertisement
print current_depth-1
