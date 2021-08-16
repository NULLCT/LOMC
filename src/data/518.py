import sys

sys.setrecursionlimit(10**7)
n, q = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dis = [-1] * n


def dfs(pair, cnt):
    for chi in g[pair]:
        if dis[chi] == -1:
            dis[chi] = cnt + 1
            dfs(chi, cnt + 1)


dis[0] = 0
dfs(0, 0)

for i in range(q):
    c, d = map(int, input().split())
    c, d = dis[c - 1], dis[d - 1]
    if (c + d) % 2 == 0:
        print("Town")
    else:
        print("Road")
