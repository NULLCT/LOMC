from collections import deque


def hukasa(graph, n):
    dist = [-1] * (n + 1)
    dist[0], dist[1] = 0, 0
    d = deque()
    d.append(1)
    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)
    return dist


N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = hukasa(graph, N)
for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[d] - dist[c]) % 2 == 0:
        print("Town")
    else:
        print("Road")
