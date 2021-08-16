import sys
from collections import deque

readline = sys.stdin.readline
split_int_readline = lambda: [int(v) for v in readline().split()]

N, Q = split_int_readline()
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = split_int_readline()
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (N + 1)
dist[1] = 0
dq = deque([1])
while len(dq) > 0:
    v = dq.popleft()
    for v2 in G[v]:
        if dist[v2] == -1:
            dq.append(v2)
            dist[v2] = dist[v] + 1

for _ in range(Q):
    c, d = split_int_readline()
    e = dist[c] + dist[d]
    if e % 2:
        print("Road")
    else:
        print("Town")
