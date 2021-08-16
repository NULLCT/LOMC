from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

q = deque()
color = [-1 for _ in range(N)]
color[0] = 0
q.append(0)

while len(q) > 0:
    node = q.popleft()
    for node2 in graph[node]:
        if color[node2] < 0:
            color[node2] = (color[node] + 1) % 2
            q.append(node2)

for _ in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
