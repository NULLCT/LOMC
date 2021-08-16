import collections as cc
import bisect as bi
import heapq as hp
import math as mt
import itertools as it
import sys

input = sys.stdin.readline
I = lambda: list(map(int, input().split()))
mod = 10**9 + 7
n, q = I()
g = cc.defaultdict(list)
for i in range(n - 1):
    a, b = I()
    g[a].append(b)
    g[b].append(a)
st = [(1, -1)]
col = [0] * (n + 1)
while st:
    now, p = st.pop()
    for then in g[now]:
        if then != p:
            col[then] = 1 ^ col[now]
            st.append((then, now))
for i in range(q):
    x, y = I()
    print("TRoowand"[not col[x] == col[y]::2])
