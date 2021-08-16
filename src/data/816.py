import queue

INF = 1000000000

N, Q = map(int, input().split())
g = [[] for _ in range(N)]

for i in range(N - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

q = queue.Queue()
dist = [INF] * N
dist[0] = 0
q.put(0)
while (not q.empty()):
    v = q.get()
    for u in g[v]:
        if (dist[u] != INF):
            continue
        dist[u] = dist[v] + 1
        q.put(u)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] == dist[d]):
        print("Town")
        continue

    print("Road" if abs(dist[c] - dist[d]) % 2 == 1 else "Town")
