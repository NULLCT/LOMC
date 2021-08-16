from collections import deque

N, Q = map(int, input().split())

edge = [[] for __ in range(N)]

for i in range(1, N):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

que = deque()
que.append(0)
color = [-1] * N
color[0] = 0

while que:
    now = que.pop()
    for adj in edge[now]:
        if color[adj] == -1:
            color[adj] = 1 - color[now]
            que.append(adj)

for i in range(Q):
    c, d = map(int, input().split())
    ans = "Town"
    if color[c - 1] != color[d - 1]:
        ans = "Road"
    print(ans)
