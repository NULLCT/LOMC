import sys

sys.setrecursionlimit(1000000)
N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1] += [b - 1]
    E[b - 1] += [a - 1]

seen = [False for _ in range(N)]
dist = [0] * N


def dfs(v, d):  # vは頂点
    seen[v] = True
    dist[v] = d
    for next_v in E[v]:
        if seen[next_v]:
            continue
        dfs(next_v, d + 1)


dfs(N - 1, 0)
for i in range(Q):
    x, y = map(int, input().split())
    if (dist[x - 1] + dist[y - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
