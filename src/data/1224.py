# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter

import sys

sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    import sys
    print(*args, file=sys.stderr)


def epp(o):
    import sys
    import pprint
    pprint.pprint(o, stream=sys.stderr)


def gen_2d_array(n, m, fill=0):
    if callable(fill):
        return [[fill() for _ in range(m)] for _ in range(n)]
    else:
        return [[fill] * m for _ in range(n)]


def gen_3d_array(n, m, k, fill=0):
    if callable(fill):
        return [[[fill() for _ in range(k)] for _ in range(m)]
                for _ in range(n)]
    else:
        return [[[fill] * k for _ in range(m)] for _ in range(n)]


def mt(f):
    import time
    import sys

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        print(e - s, 'sec', file=sys.stderr)
        return ret

    return wrap


class Doubling():
    def __init__(self, a0, M):
        """
        a0 is an array-like object which contains ai, 0 <= i < N.
        ai is the next value of i.
        """
        N = len(a0)
        self.N = N
        self.nt = [[None] * N for i in range(M.bit_length() + 1)]
        for i, a in enumerate(a0):
            self.nt[0][i] = a

        for i in range(1, len(self.nt)):
            for j in range(N):
                if self.nt[i - 1][j] is None:
                    self.nt[i][j] = None
                else:
                    self.nt[i][j] = self.nt[i - 1][self.nt[i - 1][j]]

    def apply(self, i, n):
        """
        Apply n times from i
        """
        j = i
        for k in range(n.bit_length()):
            m = 1 << k
            if m & n:
                j = self.nt[k][j]
            if j is None:
                break
        return j


class LCA():
    def __init__(self, g, root):
        s = [root]
        self.N = len(g)
        self.p = [None] * self.N
        self.d = [INF] * self.N

        self.p[root] = root
        self.d[root] = 0
        while s:
            u = s.pop()
            for v in g[u]:
                if self.d[v] is INF:
                    self.p[v] = u
                    self.d[v] = self.d[u] + 1
                    s.append(v)

        self.doubling = Doubling(self.p, self.N)

    def query(self, u, v):
        if self.d[u] > self.d[v]:
            u, v = v, u
        o = self.d[v] - self.d[u]
        v = self.doubling.apply(v, o)

        if u == v:
            return u

        for k in range(len(self.doubling.nt) - 1, -1, -1):
            if self.doubling.nt[k][u] != self.doubling.nt[k][v]:
                u = self.doubling.nt[k][u]
                v = self.doubling.nt[k][v]
        return self.doubling.nt[0][u]

    def dist(self, u, v):
        return self.d[u] + self.d[v] - 2 * self.d[self.query(u, v)]


@mt
def slv(N, Q, AB, CD):
    g = defaultdict(list)
    for a, b in AB:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    lca = LCA(g, 0)

    ans = []
    for c, d in CD:
        l = lca.dist(c - 1, d - 1)
        if l % 2 == 0:
            ans.append('Town')
        else:
            ans.append('Road')
    return ans


def main():
    N, Q = read_int_n()
    AB = [read_int_n() for _ in range(N - 1)]
    CD = [read_int_n() for _ in range(Q)]
    print(*slv(N, Q, AB, CD), sep='\n')


if __name__ == '__main__':
    main()
