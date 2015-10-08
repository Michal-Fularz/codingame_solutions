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


def propagate(current_person, persons, existing_nodes):
    depth = 1
    current_person.mark_as_visited()

    depths = []

    for neighbour in current_person.neighbours:
        index_of_neighbour = existing_nodes.index(neighbour)
        if not persons[index_of_neighbour].was_visited:
            depths.append(propagate(persons[index_of_neighbour], persons, existing_nodes))

    if len(depths) > 0:
        depth += max(depths)

    return depth

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
        persons.append(Person(xi))
        number_of_nodes += 1

    if yi not in existing_nodes:
        existing_nodes.append(yi)
        persons.append(Person(yi))
        number_of_nodes += 1

    index_of_person = existing_nodes.index(xi)
    persons[index_of_person].add_neighbour(yi)

    index_of_person = existing_nodes.index(yi)
    persons[index_of_person].add_neighbour(xi)

# for person in persons:
#     n = ""
#     for neigh in person.neighbours:
#         n += str(neigh) + ", "
#     print >> sys.stderr, str(person.get_name()) + ", neigh: " + n
#
# for node in existing_nodes:
#     print >> sys.stderr, "Nodes: " + str(node)

# lets start with first person
depths = []
for person in persons:
    depths.append(propagate(person, persons, existing_nodes))
    for person in persons:
        person.mark_as_not_visited()

for depth in depths:
    print >> sys.stderr, "Depth: " + str(depth)

# The minimal amount of steps required to completely propagate the advertisement
print min(depths)-1
