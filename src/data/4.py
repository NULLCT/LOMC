from sys import setrecursionlimit, stdin
import math

setrecursionlimit(10**7)
input = stdin.readline

N, Q = map(int, input().split())
path = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

dist = [None] * (N + 1)
dist[1] = 0
length = 0


def dfs(n, length):
    length += 1
    for v in path[n]:
        if dist[v] == None or dist[v] > length:
            dist[v] = length
            dfs(v, length)


dfs(1, 0)
for i in range(1, N + 1):
    if dist[i] % 2:
        dist[i] = 1
    else:
        dist[i] = 0

for _ in range(Q):
    c, d = map(int, input().split())
    if dist[c] == dist[d]:
        print("Town")
    else:
        print("Road")
