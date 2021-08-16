from collections import deque

INF = 10**9

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

q = deque()
dist = [-1] * N
dist[0] = 0
q.append(0)
while q:
    p = q.popleft()
    for i in G[p]:
        if dist[i] == -1:
            dist[i] = dist[p] + 1
            q.append(i)
for i in range(Q):
    a, b = map(int, input().split())
    if dist[a - 1] % 2 == dist[b - 1] % 2:
        print('Town')
    else:
        print('Road')
