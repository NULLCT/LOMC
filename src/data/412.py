import sys

sys.setrecursionlimit(100000)

N, Q = map(int, input().split())

graph = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1] += [b - 1]
    graph[b - 1] += [a - 1]

color = [0] * N


def dfs(n, d):
    if d % 2 == 0:
        color[n] = 2
    else:
        color[n] = 1

    for g in graph[n]:
        if color[g] == 0:
            dfs(g, d + 1)


dfs(0, 0)

for i in range(Q):
    c, d = map(int, input().split())

    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
