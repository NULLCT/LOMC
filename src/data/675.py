from collections import deque

N, Q = map(int, input().split())
g = [[] for _ in range(N + 1)]
ans = [[0]] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(u):
    queue = deque([u])
    d = [None] * (N + 1)
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


dist = bfs(1)
for i in range(Q):
    c, d = map(int, input().split())
    ans = abs(dist[c] - dist[d])
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
