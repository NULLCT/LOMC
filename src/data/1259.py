N, Q = map(int, input().split())
e = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

dist = [-1] * N
from collections import deque

v = deque()
v.append(0)
dist[0] = 0
while v:
    x = v.popleft()
    for ix in e[x]:
        if dist[ix] == -1:
            dist[ix] = dist[x] + 1
            v.append(ix)
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
