from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys


def input():
    return sys.stdin.readline().rstrip()


def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))


def getListGraph():
    return list(map(lambda x: int(x) - 1, input().split()))


def getArray(intn):
    return [int(input()) for i in range(intn)]


mod = 10**9 + 7
MOD = 998244353
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10**(-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############
"""
木の問題
dcを結ぶパス
"""

N, Q = getNM()
E = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = getNM()
    E[a - 1].append([b - 1, 1])
    E[b - 1].append([a - 1, 1])


def distance(n, edges, sta):
    ignore = [-1] * N  # 距離を求めたいときはfloat('inf')にする
    ignore[sta] = 0
    pos = deque([sta])

    while len(pos) > 0:
        u = pos.popleft()
        for i in edges[u]:
            if ignore[i[0]] == -1:
                ignore[i[0]] = ignore[u] + i[1]
                pos.append(i[0])
    return ignore


dis = distance(N, E, 0)
for _ in range(Q):
    c, d = getNM()
    if (dis[c - 1] + dis[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
