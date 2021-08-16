from collections import deque


def fukatan(g, n):
    dist = [-1] * (n + 1)
    dist[0], dist[1] = 0, 0
    q = deque([1])
    while q:
        v = q.popleft()
        for u in g[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            q.append(u)
    return dist


N, Q = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
dist = fukatan(g, N)
for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
