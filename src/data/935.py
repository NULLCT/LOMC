# coding: utf-8
# Your code here!
import sys

sys.setrecursionlimit(1000000)
from collections import deque

n, q = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
dist = [-1 for i in range(n)]
que = deque()
que.append((0, 0))
while que:
    v, d = que.pop()
    if dist[v] >= 0:
        continue
    dist[v] = d
    for vv in g[v]:
        que.append((vv, d + 1))
for _ in range(q):
    c, d = map(int, input().split())
    if (dist[c - 1] + dist[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
