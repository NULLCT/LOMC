n, q = map(int, input().split())  # nは頂点の数、mは辺の数

g = [[] for _ in range(n + 1)]  # 隣接リスト

for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)  #無向のみ。有向では不要

from collections import deque


def bfs(u):
    queue = deque([u])
    d = [None] * (n + 1)  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


y = bfs(1)

for i in range(q):
    p, q = map(int, input().split())
    if ((y[p] - y[q]) % 2):
        print("Road")
    else:
        print("Town")
