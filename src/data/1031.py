from collections import deque

n, Q = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
dist = [-1] * n
q = deque()
q.append(0)
dist[0] = 0
while q:
    v = q.popleft()
    for i in graph[v]:
        if dist[i] != -1: continue
        dist[i] = dist[v] + 1
        q.append(i)
# print(dist)
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[d] - dist[c]) % 2 == 0:
        print('Town')
    else:
        print('Road')
    # print(dist[c], dist[d])
