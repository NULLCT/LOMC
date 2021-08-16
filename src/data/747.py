from heapq import heappush, heappop


def dijkstra(s, n):  #（始点, ノード数）
    dist = [float('inf')] * n
    dist[s] = 0
    seen = [False] * n  #ノードの最短距離が確定済かどうか
    hq = [(0, s)]  #（距離, ノード）

    while hq:  #未確定のノードがなくなるまで
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:  #ノードvに隣接しているノードtoについて
            if not seen[to] and dist[v] + cost < dist[
                    to]:  #s→toの最短距離が未確定かつ、s→v→toの距離がs→toの暫定最短距離より短いならば
                dist[to] = dist[v] + cost  #s→toの距離をs→v→toの距離に上書き
                heappush(hq, (dist[to], to))

    return dist


N, Q = map(int, input().split())

adj = [[] for i in range(N)]  #重み付き隣接リスト
for i in range(N - 1):
    A, B = map(int, input().split())
    adj[A - 1].append((B - 1, 1))
    adj[B - 1].append((A - 1, 1))

dist = dijkstra(0, N)

for q in range(Q):
    c, d = map(int, input().split())
    x = (dist[c - 1] - dist[d - 1]) % 2
    if x == 1:
        print("Road")
    else:
        print("Town")
