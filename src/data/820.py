import sys

input = sys.stdin.readline
from heapq import heappush, heappop


def dijkstra(s, g):  # 始点・隣接グラフ
    INF = 10**18
    check = [False] * n
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)]  # 距離・ノード
    while q:
        node = heappop(q)[1]  # 今いる所までの距離・そのノード
        if check[node]: continue
        check[node] = True
        for i in g[node]:  # これから行く所までの距離・そのノード
            if check[i]: continue
            if dist[i] <= dist[node] + 1: continue
            dist[i] = dist[node] + 1
            heappush(q, [dist[i], i])
    return dist


n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

cnt = dijkstra(0, g)
for _ in range(q):
    c, d = map(int, input().split())
    if (cnt[c - 1] + cnt[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
