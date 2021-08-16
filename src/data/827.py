N, Q = map(int, input().split())
D = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    D[a].append(b)
    D[b].append(a)

INF = N + 10

Solve = [INF] * N
Solve[0] = 0

from collections import deque

d = deque([])
d.append(0)
while len(d) > 0:
    now = d.popleft()
    for to in D[now]:
        if Solve[to] == INF:
            Solve[to] = (Solve[now] + 1) % 2
            d.append(to)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    s = (Solve[c] - Solve[d]) % 2
    if s == 0:
        print("Town")
    else:
        print("Road")
