import sys

sys.setrecursionlimit(100000)

N, Q = map(int, input().split())

roads = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    roads[a - 1].append(b - 1)
    roads[b - 1].append(a - 1)

color = [-1] * N
color[0] = 0


def dfs(cur, col):
    for town in roads[cur]:
        if color[town] == -1:
            color[town] = 0 if col else 1
            dfs(town, color[town])


dfs(0, 0)
for i in range(Q):
    c, d = map(int, input().split())
    print("Town" if color[c - 1] == color[d - 1] else "Road")
