# おまじない
import sys

sys.setrecursionlimit(10000)

import math
import itertools
import queue
from collections import deque
# a, b, c, k = map(int, input().split())
# a = list(map(int, input().split()))
# s = input()
# n = int(input())
# a = map(int, input().split())
# array2 = [[False] * n for i in range(n)]

n, q = map(int, input().split())

ab = []
for i in range(n - 1):
    ai, bi = map(int, input().split())
    abi = (ai, bi)
    ab.append(abi)

cd = []
for i in range(q):
    ci, di = map(int, input().split())
    cdi = (ci, di)
    cd.append(cdi)

graph = [[] for _ in range(n + 1)]

for abi in ab:
    ai, bi = abi[0], abi[1]
    graph[ai].append(bi)
    graph[bi].append(ai)

dist = [-1] * (n + 1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

# print(dist[1:])
dist_2 = dist[1:]

color = [0] * n
for i, di in enumerate(dist_2):
    if di % 2 == 0:
        color[i] = 2
    else:
        color[i] = 1

for cdi in cd:
    ci = cdi[0] - 1
    di = cdi[1] - 1
    color_c = color[ci]
    color_d = color[di]
    if color_c == color_d:
        print("Town")
    else:
        print("Road")
