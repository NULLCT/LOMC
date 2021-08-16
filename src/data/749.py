N, W = map(int, input().split())
graph = []
for i in range(N):
    graph.append([])

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

Q = deque()
Q.append(0)
dist = [-1] * N
dist[0] = 0
while len(Q) > 0:
    x = Q.popleft()
    for y in graph[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            Q.append(y)

for i in range(W):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
