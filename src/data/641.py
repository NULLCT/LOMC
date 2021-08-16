import sys

sys.setrecursionlimit(10**6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()
nsa = lambda: list(map(str, stdin.readline().split()))
ntp = lambda: tuple(map(int, stdin.readline().split()))
mod = 10**9 + 7
inf = 10**18

n, q = na()
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = na()
    G[a].append(b)
    G[b].append(a)

import collections

que = collections.deque()
que.append(1)
color = [-1] * (n + 1)
color[1] = 0
d = {0: 1, 1: 0}
while que:
    u = que.pop()
    for v in G[u]:
        if color[v] == -1:
            color[v] = d[color[u]]
            que.append(v)

for _ in range(q):
    c, d = na()
    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')
