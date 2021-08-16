from sys import stdin
from collections import deque

n, Q = map(int, input().split())
edge = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    edge[a].append(b)
    edge[b].append(a)
colors = [-1] * n
colors[0] = 0
q = deque([0])

while q:
    v = q.popleft()
    for e in edge[v]:
        if colors[e] == -1:
            colors[e] = 1 - colors[v]
            q.append(e)
for _ in range(Q):
    c, d = map(int, stdin.readline().split())
    s = colors[c - 1]
    t = colors[d - 1]

    if s == t:
        print('Town')
    else:
        print('Road')
