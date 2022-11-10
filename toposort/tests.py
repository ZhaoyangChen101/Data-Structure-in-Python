# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
import unittest
#​‌​​​​​‌‌‌​‌​​​from model import topo_sort, Graph #Graph must be imported from a model source
from toposort import topo_sort, Graph
import random

class TestTopo(unittest.TestCase):
    #​‌​​​​​‌‌‌​‌​​​Tests for empty and singular list
    def _assert_no_back_edges(self, G, ordering):
        #​‌​​​​​‌‌‌​‌​​​ Assert that "ordering" does not have "back" edges, that is, for
        #​‌​​​​​‌‌‌​‌​​​ each vertex u in ordering there must NOT be edge u->v such that
        #​‌​​​​​‌‌‌​‌​​​ v is before u in ordering.

        #​‌​​​​​‌‌‌​‌​​​ Iterate through given vertex_list. Set "seen" contains vertices that
        #​‌​​​​​‌‌‌​‌​​​ are before the current one (u) in the given ordering.
        seen = set()
        for u in ordering:
            for n in G.neighbours(u):
                if n in seen:
                    self.fail(
                    ("A neighbour preceded its parent: vertex '{}'"
                    " was before vertex '{}' in the returned list.")
                    .format(n, u))
            seen.add(u)

    def _assert_permutation(self, G, ordering):
        """All graph vertices appear in the ordering exactly once."""

        if (len(ordering) != len(G.vertices)):
            self.fail(
            ("All vertices of input graph should appear exactly "
            "once in the ordering. However, the ordering has {} items "
            "while the graph has {} vertices.")
            .format(len(ordering), len(G.vertices)))

        V = G
        for u in V:
            countU = len([x for x in ordering if x == u])
            if countU == 1:
                continue
            else:
                self.fail(
                    ("All vertices of input graph should appear exactly "
                    "once in the ordering, but vertex '{}' appeared {} times.")
                    .format(u, countU))

    def test1_empty_graph(self):
        """Test with empty graph. (1p)"""
        emptyGraph = Graph([], [])
        emptyOrder = topo_sort(emptyGraph)
        self.assertFalse(emptyOrder,
            """Topological sort of an empty graph
                should return an empty list.
                Expected: {}
                Found: {}.""".
                format([], emptyOrder)
        )

    def test2_single_vertex(self):
        """Test with a single vertex. (1p)"""
        graph1 = Graph([1], [[]])
        order1 = topo_sort(graph1)
        self.assertListEqual(
            order1,
            [1],
            """Topological sort of a graph
                with a single vertex should return
                a list with only that vertex.
                Expected: {}
                Found: {}.""".
                format([1], order1)
        )

    def test3_simple_graph(self):
        """Test with a simple graph. (1p)"""
        V = ['a', 'b', 'c', 'd', 'e']
        A = [[2], [2,4], [3], [], [3]]
        testGraph = Graph(V, A)
        ordering = topo_sort(testGraph)
        self._assert_permutation(testGraph, ordering)
        self._assert_no_back_edges(testGraph, ordering)

    def test4_bigger_graph(self):
        """Test with a bigger graph. (1p)"""
        V = [x for x in "abcdefghijklmn"]
        A = [   [4,5,11],
                    [4,8,2],
                    [5,6,9],
                    [2,6,13],
                    [7],
                    [8,12],
                    [5],
                    [],
                    [7],
                    [10,11],
                    [13],
                    [],
                    [9],
                    []]
        testGraph = Graph(V, A)
        ordering = topo_sort(testGraph)
        self._assert_permutation(testGraph, ordering)
        self._assert_no_back_edges(testGraph, ordering)



if __name__ == '__main__':
    unittest.main(verbosity=2)

