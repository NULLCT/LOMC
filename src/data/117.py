from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dist = [float('inf') for _ in range(N)]
dist[0] = 0

data = [0]
data = deque(data)
while data:
    pos = data.popleft()
    for el in graph[pos]:
        if dist[el] == float('inf'):
            dist[el] = dist[pos] + 1
            data.append(el)

for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')