import sys
import math
import itertools
import collections
from typing import AnyStr

stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n, q = na()
root = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = na()
    root[a - 1].append(b - 1)
    root[b - 1].append(a - 1)

color = [-1] * n
color[0] = 0
que = collections.deque()
que.append(0)
while que:
    t = que.popleft()
    for nxt in root[t]:
        if color[nxt] < 0:
            color[nxt] = (color[t] + 1) % 2
            que.append(nxt)

r = []
for _ in range(q):
    c, d = na()
    if color[c - 1] == color[d - 1]:
        r.append("Town")
    else:
        r.append("Road")

for i in range(q):
    print(r[i])
