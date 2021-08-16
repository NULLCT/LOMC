# import numpy as np
import sys, math, heapq
from itertools import permutations, combinations, accumulate
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
MOD = 10**9 + 7
INF = float("inf")
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")
ceil = lambda x, y: (x + y - 1) // y
trans = lambda l: list(map(list, zip(*l)))

N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
cd = [list(map(int, input().split())) for _ in range(Q)]

edge = [[] for _ in range(N)]
color = [0] * N

for a, b in ab:
    a, b = a - 1, b - 1
    edge[a].append(b)
    edge[b].append(a)

stack = deque()
stack.append(0)
color[0] = 1
while stack:
    cindex = stack.pop()
    ccolor = color[cindex]
    # seen[cindex] = True
    ncolor = 1 - ccolor
    for nindex in edge[cindex]:
        if color[nindex] == 0:
            stack.append(nindex)
            color[nindex] = ncolor

for c, d in cd:
    c, d = c - 1, d - 1
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
