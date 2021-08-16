import queue
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(map(int, input().split()))


def ZIP(n):
    return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10**9)
INF = float('inf')
mod = 10**9 + 7
YES = 'YES'
NO = 'NO'


class Node:
    def __init__(self, n):
        self.n = n
        self.children = []

    def add_child(self, child):
        self.children = self.children + [child]


def get_find():
    visited = set()

    def find(cnt: int, dist: Node, n: Node):
        cur_c = INF
        for c in n.children:
            if c in visited:
                continue
            visited.add(c)
            if c.n == dist.n:
                return cnt
            else:
                c = find(cnt + 1, dist, c)
                cur_c = min(cur_c, c)

        return cur_c

    return find


def resolve():
    N, Q = MAP()
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    color = [-1] * N
    color[0] = 0
    que = queue.Queue()
    que.put(0)
    while not que.empty():
        t = que.get()
        for g in G[t]:
            if color[g] == -1:
                color[g] = 1 - color[t]
                que.put(g)

    for _ in range(Q):
        i, j = MAP()
        if color[i - 1] == color[j - 1]:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    resolve()
