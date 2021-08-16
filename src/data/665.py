n, q = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)

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


dd = bfs(1)
for j in range(q):
    c, d = map(int, input().split())

    if dd[c] % 2 == dd[d] % 2:
        print("Town")
    else:
        print("Road")
