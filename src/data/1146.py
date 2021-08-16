#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug


def ternary_op(flg, a, b):
    if flg:
        return a
    else:
        return b


import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
# Queue is very slow
from collections import defaultdict


class Graph:
    def __init__(self, size):
        # id starts from 0
        self.size = size
        self.vertices = [0] * size  # store depth
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = []

    def __repr__(self):
        out = []
        out.append("vertices {}".format(self.vertices))
        for i, e in enumerate(self.edges):
            out.append("{}{}".format(i, pf(e)))
        return "\n".join(out)

    def add_edge(self, frm, to):
        self.edges[frm].append(to)
        self.edges[to].append(frm)


def prepare(graph):
    visited = [False] * graph.size
    dfs(graph, 0, visited, 0)


def dfs(graph, v, visited, depth):
    visited[v] = True
    graph.vertices[v] = depth
    depth += 1
    for to in graph.edges[v]:
        if visited[to]:
            continue
        dfs(graph, to, visited, depth)


def solve(graph, c, d):
    depth_c = graph.vertices[c]
    depth_d = graph.vertices[d]
    dist_like = depth_c + depth_d
    if dist_like % 2 == 0:
        return "Town"
    else:
        return "Road"


if __name__ == '__main__':
    n, q = list(map(int, input().split()))
    graph = Graph(n)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        graph.add_edge(a, b)
    prepare(graph)
    #print('graph') # debug
    #pp(graph) # debug
    for _ in range(q):
        c, d = list(map(int, input().split()))
        c -= 1
        d -= 1
        ans = solve(graph, c, d)
        print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug
