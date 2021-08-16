N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda n: int(n) - 1, input().split())
    G[x].append(y)
    G[y].append(x)

color = [0 for _ in range(N)]


def dfs(graph, v):
    global color
    for w in graph[v]:
        if color[w] == 0:
            color[w] = color[v] * -1
            dfs(graph, w)


import sys

sys.setrecursionlimit(10**7)
color[0] = 1
dfs(G, 0)

for q in range(Q):
    c, d = map(lambda n: int(n) - 1, input().split())
    print("Town" if color[c] == color[d] else "Road")
