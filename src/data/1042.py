n, q = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
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


answer = [0] * (n + 1)
b = bfs(1)
for i in range(1, len(b)):
    if b[i] % 2 == 0:
        answer[i] = True
    else:
        answer[i] = False

for i in range(q):
    c, d = map(int, input().split())
    if answer[c] == answer[d]:
        print('Town')
    else:
        print('Road')
