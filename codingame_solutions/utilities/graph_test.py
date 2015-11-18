__author__ = 'Amin'

"""
graph_test
----------------------------------

Tests for `graph` module.
"""

import unittest

from collections import deque

from codingame_solutions.utilities.graph import Graph, GraphEdge


class GraphTest(unittest.TestCase):

    def setUp(self):
        self.g = Graph(flag_dag=True)
        self.g.add_vertex(0)
        self.g.add_vertex(1)
        self.g.add_vertex(2)
        self.g.add_edge(GraphEdge(2, 3, 1))
        self.g.add_vertex(3)
        self.g.add_edge(GraphEdge(3, 1, 1))
        self.g.add_vertex(4)
        self.g.add_edge(GraphEdge(4, 1, 1))
        self.g.add_edge(GraphEdge(4, 0, 1))
        self.g.add_vertex(5)
        self.g.add_edge(GraphEdge(5, 2, 1))
        self.g.add_edge(GraphEdge(5, 0, 1))

    def test_vertices(self):
        self.assertEqual(self.g.vertices(), [0, 1, 2, 3, 4, 5])

    def test_edges(self):
        edges = []
        edges.append(GraphEdge(2, 3, 1))
        edges.append(GraphEdge(3, 1, 1))
        edges.append(GraphEdge(4, 1, 1))
        edges.append(GraphEdge(4, 0, 1))
        edges.append(GraphEdge(5, 2, 1))
        edges.append(GraphEdge(5, 0, 1))
        self.assertEqual(self.g.edges(), edges)

    def test_topological_sorting(self):
        self.assertEqual(self.g.topological_sort(), deque([5, 4, 2, 3, 1, 0]))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
