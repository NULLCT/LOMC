from collections import deque

N, Q = map(int, input().split())
G = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

que = deque()
color = [-1] * N
color[0] = 0
que.appendleft(0)
while que:
    t = que.popleft()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.append(i)

C = []
D = []

for i in range(Q):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

for i in range(Q):
    if color[C[i] - 1] == color[D[i] - 1]:
        print("Town")
    else:
        print("Road")
