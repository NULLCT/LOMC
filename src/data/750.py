from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
# print(graph)
dist = [-1] * N
que = deque()

dist[0] = 0
que.append(0)
# print(dist)

while (len(que) != 0):
    v = que.popleft()
    for i in graph[v]:
        # print(i)
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        que.append(i)
# print(dist)
for _ in range(Q):
    c, d = map(int, input().split())
    length = abs(dist[c - 1] - dist[d - 1])
    if length % 2 == 0:
        print("Town")
    else:
        print("Road")
