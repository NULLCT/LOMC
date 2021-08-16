N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a] += b,
    G[b] += a,
from collections import deque

queue = deque([[0, 0]])
dists1 = [0 for i in range(N)]
seen = [False] * N
seen[0] = True
while queue:
    dist, node = queue.popleft()
    dist += 1
    for v in G[node]:
        if seen[v]: continue
        seen[v] = True
        dists1[v] = dist
        queue.append([dist, v])
for i in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print(["Road", "Town"][(dists1[d] + dists1[c]) % 2 == 0])
