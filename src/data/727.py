n, q = list(map(int, input().split()))

g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    g[a].append(b)
    g[b].append(a)

from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    d = [-1] * n
    d[v] = 0
    while q:
        v = q.popleft()
        for u in g[v]:
            if d[u] != -1: continue
            d[u] = d[v] + 1
            q.append(u)
    return d


a = bfs(0)

for i in range(q):
    c, d = list(map(lambda x: int(x) - 1, input().split()))

    if (a[c] - a[d]) % 2:
        print('Road')
    else:
        print('Town')
