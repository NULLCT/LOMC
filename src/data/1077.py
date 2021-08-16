import sys

sys.setrecursionlimit(10**9)
N, Q = list(map(int, input().split()))
color = [-1] * N
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
passed = [False] * N


def dfs(t, c):
    color[t] = c
    for nx in graph[t]:
        if passed[nx]: continue
        passed[nx] = True
        dfs(nx, abs(c - 1))


dfs(0, 0)
for _ in range(Q):
    c, d = list(map(int, input().split()))
    c -= 1
    d -= 1
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
