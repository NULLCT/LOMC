from collections import deque

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dist = [0 for _ in range(n)]


def bfs():
    q = deque()
    seen = [False for _ in range(n)]
    q.append([0, 0])
    while len(q) > 0:
        u, d = q.popleft()
        if seen[u]:
            continue
        seen[u] = True
        for v in g[u]:
            if seen[v]:
                continue
            q.append([v, d + 1])
            dist[v] = d + 1


bfs()
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] % 2 == dist[d] % 2:
        print('Town')
    else:
        print('Road')
