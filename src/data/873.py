from heapq import heappush, heappop

INF = 10**9


def dijkstra(s, n):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in A[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


N, Q = map(int, input().split())

A = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    A[a - 1].append((b - 1, 1))
    A[b - 1].append((a - 1, 1))

d = dijkstra(0, N)

for i in range(Q):
    a, b = map(int, input().split())
    if abs(d[a - 1] - d[b - 1]) % 2 == 1:
        print("Road")
    else:
        print("Town")
