from collections import deque


def bfs(G, s):
    Q = deque([])
    dist = [-1] * N
    dist[s] = 0
    for u in G[s]:
        dist[u] = 1
        Q.append(u)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if dist[v] != -1:
                continue
            dist[v] = dist[u] + 1
            Q.append(v)

    return dist


N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    G[A].append(B)
    G[B].append(A)

dist = bfs(G, 0)
for i in range(Q):
    C, D = map(int, input().split())
    C, D = C - 1, D - 1
    if (dist[C] - dist[D]) % 2 == 0:
        print("Town")
    else:
        print("Road")
