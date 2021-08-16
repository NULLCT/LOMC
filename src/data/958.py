import numpy as np
from functools import *
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

from collections import defaultdict

d = defaultdict(int)


def array(size, init=0):
    return [[init for j in range(size[1])] for i in range(size[0])]


def acinput():
    return list(map(int, input().split(" ")))


def dfs(x, d):
    global dist, visited
    for n in L[x]:
        if not visited[n]:
            visited[n] = True
            dist[n] = d + 1
            dfs(n, d + 1)


N, Q = acinput()

L = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = acinput()
    L[a].append(b)
    L[b].append(a)
    #print(a,b)

visited = [0] * (N + 1)
dist = [10**9] * (N + 1)
dfs(1, 0)

#print(L)
q = []
for i in range(Q):

    tmp = list(map(int, input().split(" ")))

    a = tmp[0]
    b = tmp[1]

    if (dist[b] - dist[a]) % 2 == 0:
        print("Town")
    else:
        print("Road")

#print(dp[R-1][C-1])
#print(np.array(dp))
