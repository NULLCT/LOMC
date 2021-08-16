from collections import deque

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

Que = deque()
Que.append(0)
dist = [-1] * N
dist[0] = 0
while len(Que) > 0:
    i = Que.popleft()
    for j in edge[i]:
        if dist[j] != -1:
            continue
        dist[j] = dist[i] + 1
        Que.append(j)

for i in range(Q):
    c, d = map(int, input().split())
    d = abs(dist[c - 1] - dist[d - 1])
    if d % 2 == 0:
        print('Town')
    else:
        print('Road')
