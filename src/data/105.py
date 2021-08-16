from collections import deque


def cin():
    return list(map(int, input().split()))


n, q = cin()

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = cin()
    graph[a].append(b)
    graph[b].append(a)

query = [cin() for _ in range(q)]

dist = [-1 for _ in range(n + 1)]
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

for i in range(q):
    distance = dist[query[i][0]] + dist[query[i][1]]
    if distance % 2 == 0:
        print('Town')
    else:
        print('Road')
