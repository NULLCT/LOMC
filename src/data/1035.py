#D
n, q = map(int, input().split())
g = [[] for _ in range(n)]
score = [0 for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

from collections import deque


def bfs(u):
    queue = deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


# 0からの各頂点の距離
distance = bfs(0)

for _ in range(q):
    c, d = map(int, input().split())
    if (distance[c - 1] + distance[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
