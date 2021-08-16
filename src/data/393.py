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


n, q = map(int, input().split())
el = [list(map(int, input().split())) for i in range(n - 1)]
g = [[] for _ in range(n)]
for i in range(n - 1):
    g[el[i][0] - 1].append(el[i][1] - 1)
    g[el[i][1] - 1].append(el[i][0] - 1)

d = bfs(0)
d = [i % 2 for i in d]

dic = {}
for i in range(q):
    a, b = map(int, input().split())
    if d[a - 1] == d[b - 1]:
        print("Town")
    else:
        print("Road")
