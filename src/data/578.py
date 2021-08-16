n, q = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

from collections import deque


def bfs(u):
    que = deque([u])
    l = [None] * n
    l[u] = 0
    while que:
        v = que.popleft()
        for i in g[v]:
            if l[i] is None:
                l[i] = l[v] + 1
                que.append(i)
    return l


l = bfs(0)
for i in range(n):
    l[i] %= 2

for i in range(q):
    c, d = map(int, input().split())
    if l[c - 1] == l[d - 1]:
        print("Town")
    else:
        print("Road")
