from heapq import heappush, heappop

INF = 10**9
A, B = map(int, input().split())
adj = [[] for _ in range(A)]
q = []
for i in range(A - 1):
    l, m = map(int, input().split())
    adj[l - 1].append((m - 1, 1))
    adj[m - 1].append((l - 1, 1))
for i in range(B):
    q.append(list(map(int, input().split())))


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


d = dijkstra(0, A)
for i in range(B):
    dif = d[q[i][1] - 1] - d[q[i][0] - 1]
    if dif % 2 == 0:
        print("Town")
    else:
        print("Road")
