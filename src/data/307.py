from heapq import heappush, heappop

INF = 10**9


def dijkstra(s, n, g):
    d = [INF] * n
    d[s] = 0
    hq = [(0, s)]
    while hq:
        p = heappop(hq)
        v = p[1]
        if d[v] < p[0]:
            continue
        for to, cost in g[v]:
            if d[to] > d[v] + cost:
                d[to] = d[v] + cost
                heappush(hq, (d[to], to))
    return d


n, q = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append([b - 1, 1])
    g[b - 1].append([a - 1, 1])

dij = dijkstra(0, n, g)

for i in range(q):
    c, d = map(int, input().split())
    if (dij[c - 1] + dij[d - 1]) & 1:
        print("Road")
    else:
        print("Town")
