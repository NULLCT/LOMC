from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce

sys.setrecursionlimit(2147483647)
INF = 10**13


def LI():
    return list(map(int, sys.stdin.buffer.readline().split()))


def I():
    return int(sys.stdin.buffer.readline())


def LS():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()


def S():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


def SRL(n):
    return [list(S()) for i in range(n)]


def MSRL(n):
    return [[int(j) for j in list(S())] for i in range(n)]


mod = 1000000007


class LCA(object):
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i -
                                                                       1][v]]

    def get(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.logn):  # depthの差分だけuを遡らせる
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        if u == v: return u  # 高さ揃えた時点で一致してたら終わり

        for i in range(self.logn - 1, -1, -1):  # そうでなければ上から二分探索
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]


N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    G[x - 1] += [y - 1]
    G[y - 1] += [x - 1]

lca = LCA(G)
for _ in range(Q):
    c, d = map(int, input().split())
    common = lca.get(c - 1, d - 1)
    if (lca.depth[c - 1] + lca.depth[d - 1] - 2 * lca.depth[common]) % 2 == 0:
        print("Town")
    else:
        print("Road")
