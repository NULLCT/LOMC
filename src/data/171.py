#!/usr/bin/env python3

import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = set()

    def get_next_set(self, already_visited):
        return self.neighbors - already_visited


class Graph:
    def __init__(self, N):
        self.nodes = {}
        for n in range(N):
            self.nodes[n] = Node(n)

    def add_edge(self, a, b):
        self.nodes[a].neighbors.add(b)
        self.nodes[b].neighbors.add(a)


def dfs(g, node_id, steps, answer, already_visited):
    """グラフgをnode_idを始点として深さ優先探索した結果をanswerに保存する。"""
    answer[node_id] = steps
    already_visited.add(node_id)
    next_set = g.nodes[node_id].get_next_set(already_visited)
    if len(next_set) == 0:
        return
    else:
        for next in next_set:
            dfs(g, next, steps + 1, answer, already_visited)


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, Q = list(map(int, input().split()))

    all_towns = set([n for n in range(N)])
    a = [0 for n in range(N - 1)]
    b = [0 for n in range(N - 1)]
    c = [0 for q in range(Q)]
    d = [0 for q in range(Q)]

    for n in range(N - 1):
        row = list(map(int, input().split()))
        a[n] = row[0] - 1
        b[n] = row[1] - 1

    for q in range(Q):
        row = list(map(int, input().split()))
        c[q] = row[0] - 1
        d[q] = row[1] - 1

    g = Graph(N)
    for n in range(N - 1):
        g.add_edge(a[n], b[n])

    answer = {}
    dfs(g, node_id=0, steps=0, answer=answer, already_visited=set())

    for q in range(Q):
        if (answer[c[q]] + answer[d[q]]) % 2 == 0:
            print("Town")
        else:
            print("Road")
    pass


if __name__ == '__main__':
    main()