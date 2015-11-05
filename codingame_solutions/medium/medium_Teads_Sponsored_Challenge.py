__author__ = 'Amin'

import sys
import math


class Person:
    def __init__(self, name):
        self.neighbours = []
        self.__number_of_visits = 0
        self.__name = name

    def add_neighbour(self, new_neighbour):
        self.neighbours.append(new_neighbour)

    def should_be_visited(self):
        if self.__number_of_visits < len(self.neighbours):
            return True
        else:
            return False
            
    def add_visit(self):
        self.__number_of_visits += 1
        
    def clear_visits(self):
        self.__number_of_visits = 0

    def get_name(self):
        return self.__name


def propagate(current_person, persons, existing_nodes, recurse=True):
    depth = 1
    visited_nodes = [current_person.get_name()]
    current_person.add_visit()

    depths = []
    lst_visited_nodes = []

    for neighbour in current_person.neighbours:
        if persons[neighbour].should_be_visited():
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

flag_continue = True

# lets start with first person that has one neighbour
depths = []
lst_visited_nodes = []
person_with_one_neighbour = persons[0]
for i in xrange(len(persons)):
    if len(persons[i].neighbours) == 1:
        print >> sys.stderr, "index: " + str(i)
        person_with_one_neighbour = persons[i]
        break
    
depths, lst_visited_nodes = propagate(person_with_one_neighbour, persons, existing_nodes, recurse=False)
for person in persons:
    person.clear_visits()

print >> sys.stderr, "depths: " + str(depths)
print >> sys.stderr, "lst_visited_nodes: " + str(lst_visited_nodes)

longest_list_length = len(lst_visited_nodes[0])
longest_list_index = 0
for index, lst in enumerate(lst_visited_nodes[1:]):
    if len(lst) > longest_list_length:
        longest_list_length = len(lst)
        longest_list_index = index

print >> sys.stderr, "longest_list_length: " + str(longest_list_length)
print >> sys.stderr, "longest_list_index: " + str(longest_list_index)

index_of_person_in_the_middle = longest_list_length // 2
print >> sys.stderr, "index_of_person_in_the_middle: " + str(index_of_person_in_the_middle)

person_in_the_middle = persons[0]
# find element which name == lst_visited_nodes[avg_item]
for i in xrange(len(persons)):
    if persons[i].get_name() == lst_visited_nodes[longest_list_index][index_of_person_in_the_middle]:
        person_in_the_middle = persons[i]
        break

print >> sys.stderr, "person_in_the_middle: " + str(person_in_the_middle.get_name())

depths, lst_visited_nodes = propagate(person_in_the_middle, persons, existing_nodes, recurse=False)

print >> sys.stderr, "depths: " + str(depths)
print >> sys.stderr, "lst_visited_nodes: " + str(lst_visited_nodes)

longest_list_of_visited_nodes = max([len(l) for l in lst_visited_nodes])
print >> sys.stderr, "longest_list_of_visited_nodes: " + str(longest_list_of_visited_nodes)

longest_list_length = max([len(l) for l in lst_visited_nodes])

# for depth in depths:
#     print >> sys.stderr, "Depth: " + str(depth)

# The minimal amount of steps required to completely propagate the advertisement
print longest_list_length
