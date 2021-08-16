import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(map(int, input().split()))


def TUPLE():
    return tuple(map(int, input().split()))


def ZIP(n):
    return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9 + 7
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10


class SegmentTree:
    """Segment Tree (Point Update & Range Query)
    Query
        1. update(i, val): update i-th value(0-indexed) to val
        2. query(low, high): find f(value) in [low, high)
    Complexity
        time complexity: O(log n)
        space complexity: O(n)
    """
    def __init__(self, N, f, default):  #N:要素の個数(1-indexed)
        self.N = 1 << (N -
                       1).bit_length()  #N: treeの末端の葉の数(2^n 個 n= 0, 1, 2・・・)
        self.default = default
        self.f = f
        self.segtree = [self.default] * ((self.N << 1) - 1)  #接点の数は2*N-1

    @classmethod  #self.~ とする必要がなくなる
    def create_from_array(cls, arr, f, default):
        N = len(arr)
        self = cls(N, f, default)
        for i in range(N):
            self.segtree[self.N - 1 + i] = arr[i]
        for i in reversed(range(self.N - 1)):
            self.segtree[i] = self.f(self.segtree[(i << 1) + 1],
                                     self.segtree[(i << 1) + 2])
        return self

    def update(self, i, val):  # update  i:0-indexed
        i += self.N - 1  #末端の葉に対応する位置
        self.segtree[i] = val
        while i > 0:
            i = (i - 1) >> 1  #一つ上の接点へ
            self.segtree[i] = self.f(self.segtree[(i << 1) + 1],
                                     self.segtree[(i << 1) + 2])

    def query(self, low, high):  # query l, r: 0-indexed
        # query [l, r)
        low, high = low + self.N, high + self.N
        ret = self.default
        while low < high:
            if low & 1:
                ret = self.f(ret, self.segtree[low - 1])
                low += 1
            if high & 1:
                high -= 1
                ret = self.f(ret, self.segtree[high - 1])
            low, high = low >> 1, high >> 1
        return ret

    def get(self, k):  # get k-th value(0-indexed)
        return self.segtree[k + self.N - 1]

    def all(self):  # all range query
        return self.segtree[0]


N, Q = MAP()
ab = [LIST() for _ in range(N - 1)]
cd = [LIST() for _ in range(Q)]

graph = [[] for _ in range(N)]
for a, b in ab:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

depth = [0] * (2 * N)

graph_go = [[] for _ in range(N)]
used = [0] * N
used[0] = 1
q = deque([0])
while q:
    p = q.pop()
    for node in graph[p]:
        if used[node]:
            continue
        used[node] = 1
        depth[node] = depth[p] + 1
        graph_go[p].append(node)
        q.append(node)

#print(graph)
#print(graph_go)

time = [0] * (2 * N)
when = [0] * N

used = [0] * N
used[0] = 1

q = deque([-1, 0])
t = -1
while q:
    t += 1
    p = q.pop()
    time[t] = p
    if p < 0:
        depth[p] = depth[-(p + 1)] - 1
    if p >= 0:
        when[p] = t
        for node in graph_go[p]:
            q.append(-node - 1)
            q.append(node)

depth[-1] = INF
#print("depth={}".format(depth))

#print("when={}".format(when))
#print("time={}".format(time))
lis = []
for x in time:
    lis.append(depth[x])

#print("lis= {}".format(lis))


def min_depth(A, B):
    global depth
    #print("###", A, B, depth[A], depth[B])
    if depth[int(A)] <= depth[int(B)]:
        return A
    else:
        return B


#print(min_depth(0, -3))

tree = SegmentTree.create_from_array(time, min_depth, -1)
#print(tree.segtree)

for c, d in cd:
    idx_c = when[c - 1]
    idx_d = when[d - 1]
    #print(idx_a, idx_b)
    LCA = tree.query(min(idx_c, idx_d), max(idx_c, idx_d) + 1)
    #print(LCA)

    if (depth[c - 1] + depth[d - 1] - 2 * depth[LCA]) % 2:
        print("Road")
    else:
        print("Town")
