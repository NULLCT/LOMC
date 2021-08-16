# a, b = map(int, input().split())
import heapq


def dijkstra(start, graph):
    inf = 10**18
    n = len(graph)
    dist = [inf] * n
    dist[start] = 0
    q = [(0, start)]  # q = [(startからの距離, 現在地)]
    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue
        for nx, nxd in graph[v]:
            if dist[v] + nxd < dist[nx]:
                dist[nx] = dist[v] + nxd
                heapq.heappush(q, (dist[nx], nx))
    return dist


n, q = map(int, input().split())

G = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, 1))
    G[b].append((a, 1))

dist = dijkstra(0, G)
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    tmp_dist = dist[c] + dist[d]
    if tmp_dist % 2 == 0:
        print("Town")
    else:
        print("Road")
