import sys

sys.setrecursionlimit(999999999)

n, q = map(int, input().split())
E = [[] for i in range(n + 1)]
dis = [0 for i in range(n + 1)]


def dfs(u, fa):
    dis[u] = dis[fa] + 1
    for v in E[u]:
        if v == fa:
            continue
        dfs(v, u)


for i in range(1, n):
    x, y = map(int, input().split())
    E[x].append(y)
    E[y].append(x)

dfs(1, 0)

while q:
    q -= 1
    x, y = map(int, input().split())
    print("Road" if (dis[x] + dis[y]) & 1 else "Town")
