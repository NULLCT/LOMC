N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
C, D = [0] * Q, [0] * Q
for i in range(Q):
    C[i], D[i] = map(int, input().split())

from collections import deque

d = deque([1])
depth = [-1] * (N + 1)
depth[1] = 0

while d:
    v = d.popleft()
    for i in graph[v]:
        if depth[i] != -1:
            continue
        else:
            depth[i] = (depth[v] + 1) % 2
            d.append(i)

for i in range(Q):
    if depth[C[i]] == depth[D[i]]:
        print('Town')
    else:
        print('Road')
