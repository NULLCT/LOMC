from heapq import heappush, heappop

inf = 10**9

n, q = map(int, input().split())
graph = {}
for i in range(n):
    graph[i] = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def f(s):
    que = [(0, s)]
    dist = [inf] * n
    dist[s] = 0
    while que:
        d, v = heappop(que)
        if dist[v] != d: continue
        for nv in graph[v]:
            nd = d + 1
            if dist[nv] <= nd: continue
            dist[nv] = nd
            heappush(que, (nd, nv))
    return dist


dist = f(0)

for _ in range(q):
    c, d = map(int, input().split())
    k = dist[c - 1] + dist[d - 1]
    if k % 2 == 0: print('Town')
    else: print('Road')
