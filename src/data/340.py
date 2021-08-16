N, Q = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
from collections import deque


def fukatan(g, n):
    color = [-1] * (n + 1)
    color[1] = 0
    q = deque([1])
    while q:
        v = q.popleft()
        for u in g[v]:
            if color[u] != -1:
                continue
            color[u] = (color[v] + 1) % 2
            q.append(u)
    return color


color = fukatan(g, N)
for _ in range(Q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
