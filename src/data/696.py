from collections import deque

LI = lambda: list(map(int, input().split()))
LS = lambda: list(map(str, input().split()))
MI = lambda: map(int, input().split())
MS = lambda: map(str, input().split())

N, Q = MI()
Graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = MI()
    Graph[a].append(b)
    Graph[b].append(a)

color = [-1] * (N + 1)
color[1] = 0
que = deque()
que.append(1)
while que:
    v = que.popleft()
    for u in Graph[v]:
        if color[u] != -1:
            continue
        color[u] = (color[v] + 1) % 2
        que.append(u)

for _ in range(Q):
    c, d = MI()
    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')
