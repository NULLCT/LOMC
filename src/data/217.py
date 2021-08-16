import heapq

n, q = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

INF = 10**20
Q = []
heapq.heappush(Q, (0, 0))
visited = [False] * n
visited[0] = True
dist = [INF] * n
dist[0] = 0
while len(Q) > 0:
    d, point = heapq.heappop(Q)
    for c in edges[point]:
        dd = d + 1
        if not visited[c] and dist[c] > dd:
            heapq.heappush(Q, (dd, c))
            dist[c] = dd
            visited[c] = True

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    dx = abs(dist[d] - dist[c])
    if dx % 2 == 0:
        print('Town')
    else:
        print('Road')
