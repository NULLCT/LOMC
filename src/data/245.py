from collections import deque

N, Q = map(int, input().split())
G = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
dist = [-1 for _ in range(N + 1)]
dist[1] = 0
que = deque([1])
while que:
    x = que.popleft()
    for y in G[x]:
        if dist[y] < 0:
            dist[y] = dist[x] + 1
            que.append(y)
for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
