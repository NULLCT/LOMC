N, Q = map(int, input().split())
from collections import deque

graph = [deque() for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
dist = [-1 for _ in range(N)]
dist[0] = 0
L = deque()
L.append([0, 0])
while L:
    i, s = L.popleft()
    for j in range(len(graph[i])):
        if dist[graph[i][j]] == -1:
            dist[graph[i][j]] = s + 1
            L.append([graph[i][j], s + 1])

for i in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] + dist[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
