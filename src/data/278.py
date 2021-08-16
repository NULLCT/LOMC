import heapq


def dijkstra(st):
    dst[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heapq.heappop(hq)
        if c > dst[v]: continue
        for nc, nv in G[v]:
            if c + nc >= dst[nv]: continue
            dst[nv] = c + nc
            heapq.heappush(hq, (c + nc, nv))


n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append((1, b))
    G[b].append((1, a))

dst = [float('inf')] * n
dijkstra(0)

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if abs(dst[c] - dst[d]) % 2 == 0: print('Town')
    else: print('Road')
