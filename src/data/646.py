from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N


def bfs():
    global dist
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v in G[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)


bfs()
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
