# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 21:44:36 2021

@author: kazuk
"""

from sys import setrecursionlimit

setrecursionlimit(10**7)
n, q = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

seen = [-1] * n


def dfs(v, t):
    seen[v] = t % 2
    t += 1
    for nextv in adj[v]:
        if seen[nextv] != -1:
            continue
        dfs(nextv, t)


dfs(0, 0)

for _ in range(q):
    c, d = map(int, input().split())
    if seen[c - 1] == seen[d - 1]:
        print("Town")
    else:
        print("Road")
