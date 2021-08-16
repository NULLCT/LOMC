#!/usr/bin/env python3.8
import sys
import math
from itertools import accumulate  #累積和list(accumulate(A))
from itertools import permutations
import bisect  #二分探索　bisect.bisect(A,5)
from copy import deepcopy
# import numpy as np
from collections import deque
from collections import defaultdict
from collections import Counter
from fractions import Fraction
from decimal import Decimal
from heapq import heappush, heappop

import cmath  #cmath.rect

sys.setrecursionlimit(500 * 500)

# print(' '.join(map(str, E)))


def IN():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(map(int, input().split()))


def LINE(N):
    return [list(map(int, input().split())) for _ in range(N)]


def KOSI(N):
    return [input().split() for _ in range(N)]


def Gy(gy_x, gy_mod):
    return pow(gy_x, gy_mod - 2, gy_mod)


def p_yes(judge):
    print("Yes" if judge else "No")


# MOD = 998244353
MOD = 10**9 + 7
MOD2 = 998244353

INF = 10**30 + 7
# ==================== #


def comb(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def su(x, check):
    global ans
    if check[x] == 1:
        return 0
    check[x] = 1
    ans += 1
    for lx in L[x]:
        su(lx, check)
    return 0


def root(h, w):
    if uni[h][w] == [h, w]:
        return [h, w]
    else:
        uni[h][w] = root(uni[h][w][0], uni[h][w][1])
        return uni[h][w]


def U(h, w):
    ch = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    cnt = 0
    for c in ch:
        nh = h + c[0]
        nw = w + c[1]
        if 0 <= nh < H and 0 <= nw < W and ca[nh][nw] == 1:
            if cnt == 0:
                uni[h][w] = root(nh, nw)
            else:
                uni[uni[h][w][0]][uni[h][w][1]] = root(nh, nw)
                uni[h][w] = root(nh, nw)
            cnt += 1
    if cnt == 0:
        uni[h][w] = [h, w]


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        now = heappop(hq)[1]  # ノードを pop する
        seen[now] = True
        for to, cost in v[now]:  # ノード now に隣接しているノードに対して
            if seen[to] == False and dist[now] + cost < dist[to]:
                dist[to] = dist[now] + cost
                heappush(hq, (dist[to], to))
    return dist


# ==================== #
N, Q = MAP()
v = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = MAP()
    a -= 1
    b -= 1
    v[a].append([b, 1])
    v[b].append([a, 1])
D = dijkstra(0, N)
ans = []
for i in range(Q):
    c, d = MAP()
    c -= 1
    d -= 1
    if (D[c] - D[d]) % 2 == 0:
        ans.append("Town")
    else:
        ans.append("Road")
for A in ans:
    print(A)
