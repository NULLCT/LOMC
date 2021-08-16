from heapq import heappush, heappop

INF = 10**9


def dijkstra(s, n, adj):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


n, q = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(n - 1):
    ai, bi = map(int, input().split())
    adj[ai - 1].append((bi - 1, 1))
    adj[bi - 1].append((ai - 1, 1))

dist = dijkstra(0, n, adj)

for i in range(q):
    ci, di = map(int, input().split())
    if (dist[ci - 1] + dist[di - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
