N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append((1, b - 1))
    graph[b - 1].append((1, a - 1))
ans = [0] * (N)
import heapq

hq = [(0, 0)]
g = [float('inf')] * N
g[0] = 0
while hq:
    cost, v = heapq.heappop(hq)
    if cost > g[v]:
        continue
    for dd, u in graph[v]:
        tmp = dd + g[v]
        if tmp < g[u]:
            g[u] = tmp
            heapq.heappush(hq, (tmp, u))
for i in range(N):
    if g[i] % 2 == 1:
        ans[i] = 1
dd = [0] * Q
for i in range(Q):
    c, d = map(int, input().split())
    c = c - 1
    d = d - 1
    if ans[c] != ans[d]:
        dd[i] = 1
for i in range(Q):
    if dd[i] == 0:
        print('Town')
    else:
        print('Road')
