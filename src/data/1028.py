from collections import deque


def bfs(u, g):
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


n, q = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
INF = 1001001001

dist = bfs(0, edge)
#print(dist)

for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
