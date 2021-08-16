from heapq import *

n, q = map(int, input().split())
INF = 10**9 + 7

G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def dijkstra_heap(siten):
    """
    1-indexed
    疎グラフの時に有効　O(E log(V))
    :return:
    """
    dist = [INF] * (n + 1)
    dist[siten] = 0
    que = []
    heappush(que, (dist[siten], siten))
    while len(que):
        d, v = heappop(que)
        if d > dist[v]:
            continue
        for e in G[v]:
            if dist[e] > dist[v] + 1:
                dist[e] = dist[v] + 1
                heappush(que, (dist[e], e))
    return dist


dist = dijkstra_heap(1)  #1-indexedのlist
for i in range(q):
    c, d = map(int, input().split())
    tmp = dist[c] - dist[d]
    if tmp % 2 == 0:
        print("Town")
    else:
        print("Road")
