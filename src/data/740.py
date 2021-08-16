N, Q = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N - 1)]
CD = [tuple(map(int, input().split())) for i in range(Q)]

from heapq import heappush, heappop

INF = 10**9


def dijkstra(s, n):  # (始点, ノード数, k)
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


# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(N)]
for A, B in AB:
    adj[A - 1].append((B - 1, 1))
    adj[B - 1].append((A - 1, 1))
result = dijkstra(0, N)

for c, d in CD:
    dist_c = result[c - 1]
    dist_d = result[d - 1]
    ans = dist_c - dist_d
    print("Town" if ans % 2 == 0 else "Road")
