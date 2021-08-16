from heapq import heappush, heappop

n, q = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dijkstra(s, g):  # 始点、隣接グラフ
    INF = 10**18
    check = [False] * n
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)]  # 距離・ノード
    while q:
        node = heappop(q)[1]
        if check[node]: continue
        check[node] = True
        for i in g[node]:
            if check[i]: continue
            if dist[i] <= dist[node] + 1: continue
            dist[i] = dist[node] + 1
            heappush(q, [dist[i], i])
    return dist


dis = dijkstra(0, graph)
for i in range(n):
    dis[i] %= 2

for _ in range(q):
    c, d = map(int, input().split())
    if dis[c - 1] == dis[d - 1]:
        print("Town")
    else:
        print("Road")
