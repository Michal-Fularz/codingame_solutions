__author__ = 'Amin'

import sys
import math

""" A Python Class
A simple Python graph class, demonstrating the essential facts and functionalities of graphs.
Based on:
http://www.python-course.eu/graphs_python.php
and:
https://www.python.org/doc/essays/graphs/
"""


class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict
        self.additional_info_dict = {}

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex, additional_info=None):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            self.additional_info_dict[vertex] = additional_info

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        # set makes thins strange...
        # edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

        if vertex2 not in self.__graph_dict:
            self.__graph_dict[vertex2] = []

    def __generate_edges(self):
        """ A private method generating the edges of the
            graph. Edges are represented as sets with one
            (a loop back to the vertex) or two vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def get_vertex_additional_info(self, name):
        return self.additional_info_dict[name]

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.__graph_dict:
            return None
        for node in self.__graph_dict[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.__graph_dict:
            return []
        paths = []
        for node in self.__graph_dict[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.__graph_dict:
            return None
        shortest = None
        for node in self.__graph_dict[start]:
            if node not in path:
                new_path = self.find_shortest_path(node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest

    def find_longest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.__graph_dict:
            return None
        longest = None
        for node in self.__graph_dict[start]:
            if node not in path:
                new_path = self.find_longest_path(node, end, path)
                if new_path:
                    if not longest or len(new_path) > len(longest):
                        longest = new_path
        return longest

    def find_all_paths_from_vertex(self, start, path=[]):
        """ This only works for graphs that are more like
            a tree - edges are one direction only and there
            are no loops at all
        """
        path = path + [start]
        if start not in self.__graph_dict:
            return None
        # additional stop condition to finish when in leaf
        if len(path) > 1 and len(self.__graph_dict[start]) == 1:
            return [path]
        paths = []
        for node in self.__graph_dict[start]:
            if node not in path:
                new_paths = self.find_all_paths_from_vertex(node, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def get_vertices_with_n_edges(self, n):
        vertices_with_n_edges = []
        for key, values in self.__graph_dict.items():
            if len(values) == n:
                vertices_with_n_edges.append(key)

        return vertices_with_n_edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\n"
        res += "edges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


class Stop:
    def __init__(self, identifier, full_name, latitude, longitude, type):
        self.identifier = identifier
        self.full_name = full_name
        self.latitude = latitude
        self.longitude = longitude
        self.type = type

    def __str__(self):
        res = ""
        res += str(self.identifier) + ", "
        res += str(self.full_name) + ", "
        res += str(self.latitude) + ", "
        res += str(self.longitude) + ", "
        res += str(self.type)

        return res


def calc_distance(latitudeA, longitudeA, latitudeB, longitudeB):
    x = (longitudeB - longitudeA) * math.cos((latitudeA + latitudeB) / 2)
    y = latitudeB - latitudeA
    d = math.sqrt(x*x + y*y) * 6371
    return d

start_point = input()
end_point = input()
n = int(input())

g = Graph()

for i in range(n):
    stop_name = input()
    elements = stop_name.split(",")

    new_stop_info = Stop(elements[0], elements[1].replace('"', ""), elements[3], elements[4], elements[7])
    #print("new_stop_info: " + str(new_stop_info), file=sys.stderr)
    g.add_vertex(new_stop_info.identifier, new_stop_info)

m = int(input())
for i in range(m):
    route = input()
    stops = route.split(" ")
    g.add_edge((stops[0], stops[1]))

#print(g, file=sys.stderr)

shortest_path = g.find_all_paths(start_point, end_point)

print("shortest_path: " + str(shortest_path), file=sys.stderr)

r = ""
for stop in shortest_path:
    r += g.get_vertex_additional_info(stop).full_name + "\n"

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(r[:-1])
