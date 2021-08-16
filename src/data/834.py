import sys

n, qq = map(int, input().split())

g = [[] * 2 for i in range(n)]

for i in range(n - 1):
    ai, bi = map(int, input().split())
    g[ai - 1].append(bi - 1)
    g[bi - 1].append(ai - 1)

seen = [False] * n
q = []

d = [0] * n

v = 0
q.append(v)
seen[v] = True
while q:
    next_v = q.pop()
    for v2 in g[next_v]:
        if seen[v2]:
            continue
        q.append(v2)
        seen[v2] = True
        d[v2] = d[next_v] + 1

for i in range(qq):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    if (d[ci] + d[di]) % 2 == 0:
        print("Town")
    else:
        print("Road")
