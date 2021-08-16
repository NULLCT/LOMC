from heapq import heappush, heappop

INF = 10**9


def dijkstra(s, n):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


# ノード数, エッジ数, 始点ノード
n, m = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(n)]
for i in range(n - 1):
    s, t = map(int, input().split())
    s, t = s - 1, t - 1
    adj[s].append((t, 1))
    adj[t].append((s, 1))

dis = dijkstra(0, n)
for _ in range(m):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    dif = dis[c] - dis[d]
    if dif % 2 == 0:
        print('Town')
    else:
        print('Road')
