N, Q = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N - 1)]
cd = [tuple(map(int, input().split())) for _ in range(Q)]

connect = [[] for _ in range(N)]
for a, b in ab:
    connect[a - 1].append(b - 1)
    connect[b - 1].append(a - 1)

INF = 10**10
cost = [INF] * N

from collections import deque

cost[0] = 0
queue = deque([(cost[0], 0)])
while queue:
    c, v = queue.popleft()

    for u in connect[v]:
        if cost[u] == INF:  # u is not visited
            cost[u] = c + 1
            queue.append((c + 1, u))

# print( cost )
for c, d in cd:
    if cost[c - 1] % 2 == cost[d - 1] % 2:
        print("Town")
    else:
        print("Road")
