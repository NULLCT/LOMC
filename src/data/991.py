from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1] * N
que = deque([0])
dist[0] = 0

while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)

q = [] * Q
for i in range(Q):
    c, d = map(int, input().split())
    q.append([c - 1, d - 1])

for i in range(Q):
    if abs(dist[q[i][1]] - dist[q[i][0]]) % 2 == 0:
        print('Town')
    else:
        print('Road')
