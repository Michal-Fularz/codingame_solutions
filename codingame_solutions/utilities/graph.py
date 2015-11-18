__author__ = 'Amin'

from collections import deque, namedtuple


GraphEdge = namedtuple("GraphEdge", "starting_vertex, ending_vertex, distance")
EdgeProperties = namedtuple("EdgeProperties", "destitantion_vertex, distance")


class Graph(object):
    """
    A simple Python graph class, demonstrating the essential facts and functionalities of graphs.
    Based on:
    http://www.python-course.eu/graphs_python.php
    and:
    https://www.python.org/doc/essays/graphs/
    """

    def __init__(self, graph_dict={}, flag_dag=False):
        """
        :param graph_dict:
        :param flag_dag: flag indicating if the graph is a Directed Acyclic Graph
        :return:
        """
        self.flag_DAG = flag_dag

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

    def add_edge(self, edge: GraphEdge):
        """ between two vertices can be multiple edges!
        """
        if edge.starting_vertex in self.__graph_dict:
            self.__graph_dict[edge.starting_vertex].append(EdgeProperties(edge.ending_vertex, edge.distance))
        else:
            self.__graph_dict[edge.ending_vertex] = [EdgeProperties(edge.ending_vertex, edge.distance)]

        if edge.ending_vertex not in self.__graph_dict:
            self.__graph_dict[edge.ending_vertex] = []

    def __generate_edges(self):
        """ A private method generating the edges of the
            graph. Edges are represented as GraphEdge namedtuple
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append(GraphEdge(vertex, neighbour.destitantion_vertex, neighbour.distance))
        return edges

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
            It means that a graph is DAG
        """
        if self.flag_DAG:
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
        else:
            raise ValueError("This method only works for DAG!")

    def __topological_sort_util(self, key, visited, stack):
        visited[key] = True

        for neighbour in self.__graph_dict[key]:
            if not visited[neighbour.destitantion_vertex]:
                self.__topological_sort_util(neighbour.destitantion_vertex, visited, stack)

        stack.appendleft(key)

    def topological_sort(self) -> deque:
        """
        Based on:
        http://www.geeksforgeeks.org/topological-sorting/
        :return:
        """
        if self.flag_DAG:
            stack = deque(maxlen=len(self.__graph_dict))
            visited = {}

            for key in self.__graph_dict:
                visited[key] = False

            for key in self.__graph_dict:
                if not visited[key]:
                    self.__topological_sort_util(key, visited, stack)

            return stack
        else:
            raise ValueError("This method only works for DAG!")

    def find_longest_path(self, starting_vertex):
        """
        Based on:
        http://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
        The method find longest distances from a given vertex. It uses
        recursive topological_sort() to get topological sorting.
        :param starting_vertex:
        :return:
        """
        if self.flag_DAG:
            stack = self.topological_sort()

            min_distance = -1
            distances = {}

            for key in self.__graph_dict:
                distances[key] = min_distance

            distances[starting_vertex] = 0

            while len(stack) > 0:
                vertex = stack.popleft()

                if distances[vertex] != min_distance:
                    for neighbour in self.__graph_dict[vertex]:
                        n_name = neighbour.destitantion_vertex
                        n_dist = neighbour.distance
                        if distances[n_name] < distances[vertex] + n_dist:
                            distances[n_name] = distances[vertex] + n_dist

            return distances

        else:
            raise ValueError("This method only works for DAG!")

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


if __name__ == "__main__":
    # TODO: use unit test to test this module

    # g = { "a" : ["d", "e"],
    #       "b" : ["c"],
    #       "c" : ["b", "c", "d", "e"],
    #       "d" : ["a", "c"],
    #       "e" : ["c", "b"],
    #       "f" : []
    #     }
    #
    # graph = Graph(g)
    #
    # print("Vertices of graph:")
    # print(graph.vertices())
    #
    # print("Edges of graph:")
    # print(graph.edges())
    #
    # print("Add vertex:")
    # graph.add_vertex("z")
    #
    # print("Vertices of graph:")
    # print(graph.vertices())
    #
    # print("Add an edge:")
    # graph.add_edge({"a", "z"})
    #
    # print("Vertices of graph:")
    # print(graph.vertices())
    #
    # print("Edges of graph:")
    # print(graph.edges())
    #
    # print('Adding an edge {"x","y"} with new vertices:')
    # graph.add_edge({"x", "y"})
    # print("Vertices of graph:")
    # print(graph.vertices())
    # print("Edges of graph:")
    # print(graph.edges())
    #
    # print("Find path between a and b:")
    # print(graph.find_path("a", "b"))
    #
    # print("Find all paths between a and b:")
    # print(graph.find_all_paths("a", "b"))
    #
    # print("Find shortest path between a and b:")
    # print(graph.find_shortest_path("a", "b"))
    #
    # print("Find logest path between a and b:")
    # print(graph.find_longest_path("a", "b"))
    #
    # g = { "0" : ["1"],
    #       "1" : ["0", "2"],
    #       "2" : ["1", "3", "4"],
    #       "3" : ["2"],
    #       "4" : ["2"],
    #     }
    #
    # graph = Graph(g)

    graph = Graph()
    graph.add_edge(("0", "1"))
    graph.add_edge(("1", "0"))
    graph.add_edge(("1", "2"))
    graph.add_edge(("2", "1"))
    graph.add_edge(("2", "3"))
    graph.add_edge(("3", "2"))
    graph.add_edge(("2", "4"))
    graph.add_edge(("4", "2"))

    print(graph)

    print("Find all paths from 0:")
    print(graph.find_all_paths_from_vertex("0"))

    print("Vertices with 1 neighbour:")
    vertices_with_1_edge = graph.get_vertices_with_n_edges(1)
    print(vertices_with_1_edge)
    print(vertices_with_1_edge[1])
