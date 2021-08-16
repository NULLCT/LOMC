n, q = map(int, input().split())
e = [[] for _ in range(n)]

import heapq


def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq)
    cost = [float('inf')] * n
    cost[s] = 0

    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost


for i in range(n - 1):
    a, b = map(int, input().split())
    e[a - 1].append((1, b - 1))
    e[b - 1].append((1, a - 1))

dist = dijkstra(0)

for j in range(q):
    c, d = map(int, input().split())
    x = abs(dist[c - 1] - dist[d - 1])
    if x % 2 == 1:
        print('Road')
    else:
        print('Town')
