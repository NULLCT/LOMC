from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
color = [-1] * N
color[0] = 0
d = deque([0])
while d:
    v = d.pop()
    for n in G[v]:
        if color[n] == -1:
            color[n] = 1 - color[v]
            d.append(n)
for _ in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
