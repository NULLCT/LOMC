import heapq as hq
import math

N, Q = [int(_) for _ in input().split(' ')]


def dijkstra(G, s):
    n = len(G)
    visited = [False] * n
    weights = [math.inf] * n
    path = [None] * n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights


G = []
for i in range(N):
    G.append([])
for i in range(N - 1):
    a, b = [int(_) for _ in input().split(' ')]
    G[a - 1].append((b - 1, 1))
    G[b - 1].append((a - 1, 1))

alls = dijkstra(G, 0)[1]

for i in range(Q):
    k, v = [int(_) for _ in input().split(' ')]
    print("Road" if (alls[k - 1] - alls[v - 1]) % 2 else "Town")
