from collections import deque

n, q = map(int, input().split())
G = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0
que = deque()
que.append(1)
while que:
    v = que.popleft()
    for i in G[v]:
        if dist[i] > -1:
            continue
        dist[i] = dist[v] + 1
        que.append(i)
for j in range(q):
    c, d = map(int, input().split())
    if dist[c] % 2 == 0 and dist[d] % 2 == 0 or dist[c] % 2 == 1 and dist[
            d] % 2 == 1:
        print('Town')
    else:
        print('Road')
