from sys import stdin
from sys import stdout
from sys import setrecursionlimit

import math
import collections
import heapq
import itertools
import functools


def printf(elem):
    stdout.write(str(elem) + "\n")


def printline(iter):
    stdout.write(" ".join(map(str, iter)) + "\n")


def readcontainer(type=int, container=list):
    return container(map(type, stdin.readline().split()))


def readigits(type=int, container=list):
    return container(map(type, stdin.readline()[:-1]))


def readnum(type=int):
    return type(stdin.readline())


def readline():
    return stdin.readline()[:-1]


setrecursionlimit(1000000)


def dfs(G, start, visited, colors):
    if not visited[start]:
        visited[start] = True
        for v in G[start]:
            colors[v] = not colors[start]
            dfs(G, v, visited, colors)


## Do stuff!! :)
n, q = readcontainer()
g = [set() for _ in range(n + 2)]
for _ in range(n - 1):
    a, b = readcontainer()
    g[a].add(b)
    g[b].add(a)

visited = [False for _ in range(n + 2)]
colors = [False for _ in range(n + 2)]

colors[1] = True
dfs(g, 1, visited, colors)

for _ in range(q):
    c, d = readcontainer()
    if colors[c] == colors[d]:
        printf("Town")
    else:
        printf("Road")
