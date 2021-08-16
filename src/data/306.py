from collections import deque

n, Q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(0)

d = [-1] * n
d[0] = 0

while q:
    v = q.popleft()
    for nv in g[v]:
        if d[nv] == -1:
            d[nv] = d[v] + 1
            q.append(nv)

for i in range(Q):
    C, D = map(int, input().split())
    C -= 1
    D -= 1
    if (d[C] + d[D]) % 2:
        print("Road")
    else:
        print("Town")