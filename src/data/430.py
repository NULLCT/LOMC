from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

color = [-1] * N
color[0] = 0
q = deque()
q.append(0)

while len(q):
    t = q.popleft()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            q.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
